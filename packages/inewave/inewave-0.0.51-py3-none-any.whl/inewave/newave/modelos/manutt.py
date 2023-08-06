from inewave._utils.bloco import Bloco
from inewave._utils.leiturablocos import LeituraBlocos

from typing import List


class LeituraManutT(LeituraBlocos):
    """
    Realiza a leitura do arquivo `manutt.dat`
    existente em um diretório de entradas do NEWAVE.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo `manutt.dat`, construindo
    um objeto `ManutT` cujas informações são as mesmas do manutt.dat.

    Este objeto existe para retirar do modelo de dados a complexidade
    de iterar pelas linhas do arquivo, recortar colunas, converter
    tipos de dados, dentre outras tarefas necessárias para a leitura.
    """

    def __init__(self, diretorio: str):
        super().__init__(diretorio)

    # Override
    def _cria_blocos_leitura(self) -> List[Bloco]:
        """
        Cria a lista de blocos a serem lidos no arquivo manutt.dat.
        """
        return []
