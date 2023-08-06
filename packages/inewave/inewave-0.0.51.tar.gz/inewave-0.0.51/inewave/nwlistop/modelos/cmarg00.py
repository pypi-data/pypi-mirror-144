# Imports do próprio módulo
from inewave._utils.leiturablocos import LeituraBlocos
from inewave._utils.bloco import Bloco
from inewave._utils.registros import RegistroAn, RegistroFn, RegistroIn
from inewave.config import MAX_ANOS_ESTUDO, MESES_DF, NUM_CENARIOS
from inewave.config import NUM_PATAMARES, MESES

# Imports de módulos externos
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from typing import IO, List


class BlocoCmargPatamarAno(Bloco):
    """
    Bloco com as informações das tabelas de custo marginal
    por patamar e por mês/ano de estudo.
    """

    str_inicio = "CUSTO MARGINAL DE DEMANDA ($/MWh)"
    str_fim = ""

    def __init__(self):

        super().__init__(BlocoCmargPatamarAno.str_inicio, "", True)

        self._dados = ["", pd.DataFrame()]

    def __eq__(self, o: object):
        if not isinstance(o, BlocoCmargPatamarAno):
            return False
        bloco: BlocoCmargPatamarAno = o
        return all(
            [
                self._dados[0] == bloco.dados[0],
                self._dados[1].equals(bloco._dados[1]),
            ]
        )

    # Override
    def le(self, arq: IO):
        def converte_tabela_em_df() -> pd.DataFrame:
            df = pd.DataFrame(tabela)
            df.columns = MESES_DF + ["Média"]
            df["Ano"] = anos
            df["Série"] = serie
            df["Patamar"] = patamar
            df = df[["Ano", "Série", "Patamar"] + MESES_DF + ["Média"]]
            return df

        # Salta a primeira linha
        arq.readline()
        # Variáveis auxiliares
        anos = np.zeros(
            (NUM_CENARIOS * MAX_ANOS_ESTUDO * NUM_PATAMARES,), dtype=np.int64
        )
        serie = np.zeros(
            (NUM_CENARIOS * MAX_ANOS_ESTUDO * NUM_PATAMARES,), dtype=np.int64
        )
        patamar = np.zeros(
            (NUM_CENARIOS * MAX_ANOS_ESTUDO * NUM_PATAMARES,), dtype=np.int64
        )
        tabela = np.zeros(
            (NUM_CENARIOS * MAX_ANOS_ESTUDO * NUM_PATAMARES, len(MESES_DF) + 1)
        )
        reg_mercado = RegistroAn(12)
        reg_ano = RegistroIn(4)
        reg_serie = RegistroIn(4)
        reg_patamar = RegistroIn(3)
        reg_cmarg = RegistroFn(8)
        i = 0
        ano = 0
        # Identifica o submercado
        self._dados[0] = reg_mercado.le_registro(self._linha_inicio, 70)
        while True:
            linha = arq.readline()
            # Confere se acabou
            if len(linha) == 0:
                anos = anos[:i]
                serie = serie[:i]
                patamar = patamar[:i]
                tabela = tabela[:i, :]
                self._dados[1] = converte_tabela_em_df()
                break
            # Confere se acabou uma tabela
            if "  MEDIA   " in linha:
                ano = 0
            # Confere se começou uma tabela
            if "     ANO: " in linha:
                ano = reg_ano.le_registro(linha, 10)
                # Pula a linha de cabeçalhos
                arq.readline()
            # Se está numa tabela, lê
            elif ano != 0:
                anos[i] = ano
                if not linha[2:6].strip().isnumeric():
                    serie[i] = serie[i - 1]
                else:
                    serie[i] = reg_serie.le_registro(linha, 2)
                patamar[i] = reg_patamar.le_registro(linha, 8)
                tabela[i, :] = reg_cmarg.le_linha_tabela(
                    linha, 15, 1, len(MESES) + 1
                )
                i += 1

    # Override
    def escreve(self, arq: IO):
        pass


class LeituraCmarg00(LeituraBlocos):
    """
    Realiza a leitura dos arquivos cmarg00x.out
    existentes em um diretório de saídas do NEWAVE.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de arquivos cmarg00x.out, construindo
    objetos `Cmarg00` cujas informações são as mesmas dos arquivos.

    Este objeto existe para retirar do modelo de dados a complexidade
    de iterar pelas linhas do arquivo, recortar colunas, converter
    tipos de dados, dentre outras tarefas necessárias para a leitura.
    """

    def __init__(self, diretorio: str) -> None:
        super().__init__(diretorio)

    def _cria_blocos_leitura(self) -> List[Bloco]:
        return [BlocoCmargPatamarAno()]
