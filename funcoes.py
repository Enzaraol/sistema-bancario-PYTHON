import PySimpleGUI as sg
lista = [{'nome': 'enzo', 'senha': '123'}]
dados = {}
posicao = 0
def janela_login():
    layout = [
        [sg.Text('Login')],
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Cadastro'), sg.Button('Login'), sg.Button('Armaz.')],
        ]

    return sg.Window('Loginzinho', layout, finalize=True)

def janela_cadastro():
    lay2 = [
        [sg.Text('Novo Cadastro')],
        [sg.Input(key='nusuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Salvar'), sg.Button('Voltar')]
            ]
    return sg.Window('Novo Cadastro', lay2, finalize=True)

def janela_armaz():
    lay3 = [
        [sg.Text('Veja os DADOS')],
        [sg.Button('Voltar')]]
    return sg.Window('Armazenamento',  lay3, finalize=True)

def janela_acesso():
    lay4 = [
        [sg.Text('Olá! Seja Bem-Vindo(a)')],
        [sg.Button('SAQUE'), sg.Button('DEPÓSITO')],
        [sg.Button('SAIR')]
    ]
    return sg.Window('ACESSO PRINCIPAL', lay4, finalize=True)

def janela_deposito():
    lay5 = [
        [sg.Text('DEPÓSITO'), sg.Input(key='deposito')],
        [sg.Text('SENHA'), sg.Input(key='senha')],
        [sg.Button('VOLTAR')],
        [sg.Button('SALVAR')]
    ]
    return sg.Window('JANELA DEPÓSITO', lay5, finalize=True)

def janela_saque():
    lay6 = [
        [sg.Text('SAQUE'), sg.Input(key='saque')],
        [sg.Text('SENHA'), sg.Input(key='senha')],
        [sg.Button('SALVAR'), sg.Button('VOLTAR')]
    ]
    return sg.Window('SAQUE', lay6, finalize=True)

