from dao.abstractDao import DAO
from entidade.partida import Partida


class PartidaDAO(DAO):
    def __init__(self):
        super().__init__('partida.pkl')

    def add(self, partida: Partida):
        if (isinstance(Partida.codigo, int)) and (partida is not None) and isinstance(partida, Partida):
            super().add(partida.codigo, partida)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
