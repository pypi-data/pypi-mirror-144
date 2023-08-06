from typing import List


from inewave._utils.escritablocos import EscritaBlocos

from inewave._utils.dadosarquivo import DadosArquivoBlocos
from inewave._utils.arquivo import ArquivoBlocos
from inewave.nwlistcf.modelos.estados import LeituraEstados
from inewave.nwlistcf.modelos.estados import RegistroEstado


class Estados(ArquivoBlocos):
    """
    Armazena os dados dos estados visitados pelo NEWAVE existentes
    no arquivo `estados.rel` do NWLISTCF.

    Esta classe armazena os estados de cada uma das variáveis envolvidas
    no problema e da função objetivo, para cada registro e REE dentro
    do registro.

    Cada registro possui um modelo próprio, armazenando os estados das
    variáveis em uma array específica.

    """

    def __init__(self, dados: DadosArquivoBlocos):
        super().__init__(dados)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="estados.rel"
    ) -> "Estados":
        leitor = LeituraEstados(diretorio)
        r = leitor.le_arquivo(nome_arquivo)
        return cls(r)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="estados.rel"):
        escritor = EscritaBlocos(diretorio)
        escritor.escreve_arquivo(self._dados, nome_arquivo)

    @property
    def registros(self) -> List[RegistroEstado]:
        registros: List[RegistroEstado] = []
        for b in self._blocos:
            registros += b.dados
        return registros
