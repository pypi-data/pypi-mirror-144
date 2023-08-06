from inewave.newave.modelos.confhd import BlocoConfUHE
from inewave.newave.modelos.confhd import LeituraConfhd
from inewave._utils.dadosarquivo import DadosArquivoBlocos
from inewave._utils.arquivo import ArquivoBlocos
from inewave._utils.escritablocos import EscritaBlocos


import pandas as pd  # type: ignore


class Confhd(ArquivoBlocos):
    """
    Armazena os dados de entrada do NEWAVE referentes às
    configurações das usinas hidrelétricas.

    Esta classe lida com informações de entrada fornecidas ao NEWAVE e
    que podem ser modificadas através do arquivo `modif.dat`.

    """

    def __init__(self, dados: DadosArquivoBlocos):
        super().__init__(dados)
        # Interpreta o resultado da leitura
        val = True
        msg = "Erro na criação de Confhd: "
        if len(dados.blocos) == 1:
            bloco = dados.blocos[0]
            if isinstance(bloco, BlocoConfUHE):
                self.__bloco = bloco
            else:
                msg += (
                    f"O bloco deve ser do tipo {BlocoConfUHE}, "
                    + f"mas foi fornecido do tipo {type(bloco)}"
                )
                val = False
        else:
            msg += "Deve ser fornecido exatamente 1 bloco para Confhd"
            val = False
        if not val:
            raise TypeError(msg)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="confhd.dat") -> "Confhd":
        """ """
        leitor = LeituraConfhd(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="confhd.dat"):
        """ """
        escritor = EscritaBlocos(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    @property
    def usinas(self) -> pd.DataFrame:
        return self.__bloco.dados

    @usinas.setter
    def usinas(self, d: pd.DataFrame):
        self.__bloco.dados = d
