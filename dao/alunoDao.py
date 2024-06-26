from dao.abstractDao import DAO
from entidade.aluno import Aluno


class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if (isinstance(aluno.cpf, int)) and (aluno is not None) and isinstance(aluno, Aluno):
            super().add(aluno.codigo, aluno)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
