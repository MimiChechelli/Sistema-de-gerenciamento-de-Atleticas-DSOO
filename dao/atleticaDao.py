from dao.abstractDao import DAO
from entidade.atletica import Atletica


class AtleticaDAO(DAO):
    def __init__(self):
        super().__init__('atletica.pkl')

    def add(self, atletica: Atletica):
        if (isinstance(Atletica.curso, str)) and (atletica is not None) and isinstance(atletica, Atletica):
            super().add(atletica.curso, atletica)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
