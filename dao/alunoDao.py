from abstractDao import DAO
from entidade.aluno import Aluno
class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')
    
    def add(self, aluno: Aluno):
        if (isinstance(aluno.cpf, int)) and (aluno is not None) and isinstance(aluno, Aluno):
            super().add(aluno.codigo, aluno)
            #parei no slide 21
