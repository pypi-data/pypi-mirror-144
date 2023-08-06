from typing import List

from inewave._utils.escritablocos import EscritaBlocos

from inewave._utils.dadosarquivo import DadosArquivoBlocos
from inewave._utils.arquivo import ArquivoBlocos
from inewave.nwlistcf.modelos.nwlistcf import LeituraNwlistcf
from inewave.nwlistcf.modelos.nwlistcf import RegistroNwlistcf


class Nwlistcf(ArquivoBlocos):
    """
    Armazena os dados dos cortes construídos pelo NEWAVE existentes
    no arquivo `nwlistcf.rel` do NWLISTCF.

    Esta classe armazena os cortes da FCF de cada uma das variáveis,
    para cada registro e REE dentro do registro.

    Cada registro possui um modelo próprio, armazenando os coeficientes
    dos hiperplanos em uma array específica.

    """

    def __init__(self, dados: DadosArquivoBlocos):
        super().__init__(dados)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="nwlistcf.rel"
    ) -> "Nwlistcf":
        leitor = LeituraNwlistcf(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="nwlistcf.rel"):
        escritor = EscritaBlocos(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    @property
    def registros(self) -> List[RegistroNwlistcf]:
        registros: List[RegistroNwlistcf] = []
        for b in self._blocos:
            registros += b.dados
        return registros
