from dao.abstractDao import DAO
from entidade.arbitro import Arbitro


class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitro.pkl')

    def add(self, arbitro: Arbitro):
        if (isinstance(Arbitro.cpf, int)) and (arbitro is not None) and isinstance(arbitro, Arbitro):
            super().add(arbitro.cpf, arbitro)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
