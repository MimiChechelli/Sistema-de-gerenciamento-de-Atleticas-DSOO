from dao.abstractDao import DAO
from entidade.campeonato import Campeonato


class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonato.pkl')

    def add(self, campeonato: Campeonato):
        if (isinstance(Campeonato.edicao, int)) and (campeonato is not None) and isinstance(campeonato, Campeonato):
            super().add(campeonato.edicao, campeonato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
