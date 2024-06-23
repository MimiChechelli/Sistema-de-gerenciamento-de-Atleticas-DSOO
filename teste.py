import PySimpleGUI as sg

# Estrutura de uma atlética
class Atletica:
    def __init__(self, nome, curso, alunos):
        self.nome = nome
        self.curso = curso
        self.alunos = alunos

def selecionar_atletica_por_curso(lista_atleticas):
    # Extrair os cursos únicos
    cursos = sorted(set(atletica.curso for atletica in lista_atleticas))
    
    # Layout inicial para selecionar o curso
    layout_curso = [
        [sg.Text('Selecione o Curso')],
        [sg.Listbox(values=cursos, size=(30, 6), key='curso_selecionado')],
        [sg.Button('Selecionar Curso')]
    ]
    
    window = sg.Window('Seleção de Curso').Layout(layout_curso)
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        window.close()
        return None

    curso_selecionado = valores['curso_selecionado'][0] if valores['curso_selecionado'] else None
    window.close()

    if not curso_selecionado:
        return None

    # Filtrar atléticas pelo curso selecionado
    atleticas_filtradas = [atletica.nome for atletica in lista_atleticas if atletica.curso == curso_selecionado]
    
    # Layout para selecionar a atlética
    layout_atletica = [
        [sg.Text(f'Atléticas do curso: {curso_selecionado}')],
        [sg.Listbox(values=atleticas_filtradas, size=(30, 6), key='atletica_selecionada')],
        [sg.Button('Selecionar Atlética')]
    ]
    
    window = sg.Window('Seleção de Atlética').Layout(layout_atletica)
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        window.close()
        return None

    atletica_selecionada = valores['atletica_selecionada'][0] if valores['atletica_selecionada'] else None
    window.close()

    return atletica_selecionada

# Exemplo de uso:
lista_atleticas = [
    Atletica("Atlética A", "Engenharia", ["Aluno 1", "Aluno 2"]),
    Atletica("Atlética B", "Direito", ["Aluno 3", "Aluno 4"]),
    Atletica("Atlética C", "Medicina", ["Aluno 5", "Aluno 6"]),
    Atletica("Atlética D", "Engenharia", ["Aluno 7", "Aluno 8"]),
]

atletica_escolhida = selecionar_atletica_por_curso(lista_atleticas)
if atletica_escolhida:
    print(f'Atlética escolhida: {atletica_escolhida}')
else:
    print('Nenhuma atlética foi selecionada.')
