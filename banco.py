from funcoes import *

janela1, jcadastro, jarmaz, jacesso, jdeposito, jsaque = janela_login(), None, None, None, None, None
while True:
    window, evento, valor = sg.read_all_windows()
    s = 0
    if window == janela1 and evento == sg.WIN_CLOSED:
        break
    elif window == janela1 and evento == 'Cadastro':
        jcadastro = janela_cadastro()
        jcadastro.un_hide()
    elif window == janela1 and evento == 'Armaz.':
        jarmaz = janela_armaz()
        jarmaz.un_hide()
        print(lista)
    elif window == jcadastro and evento == 'Salvar':
        dados['nome'] = valor['nusuario']
        dados['senha'] = valor['senha']
        lista.append(dados.copy()), dados.clear()
        jcadastro.hide()
    elif window == jcadastro and evento == 'Voltar' or evento == sg.WIN_CLOSED:
        jcadastro.hide()
    elif window == jarmaz and evento == 'Voltar' or evento == sg.WIN_CLOSED:
        jarmaz.hide()

    elif window == janela1 and evento == 'Login':
        n1 = valor['usuario']
        n2 = valor['senha']
        for pos, l in enumerate(lista):
            if n1 == l["nome"] and n2 == l["senha"]:
                jacesso = janela_acesso()
                jacesso.un_hide()
                s += 1
                #Armazeno a posição em uma variável para chama-lá posteriormente
                posicao += pos
                break
        if s == 0:
            sg.Popup(f'Usuário não cadastrado')


#JANELA DE DEPÓSITO
    elif window == jacesso and evento == 'DEPÓSITO':
        jdeposito = janela_deposito()
        jdeposito.un_hide()
    elif window == jdeposito and evento == 'SALVAR':
        s = valor['senha']
        lsenha = lista[posicao]['senha']
        if s == lsenha:
            valor = valor['deposito']
            lista[posicao]['saldo'] = int(valor)
            sg.Popup('VALOR DEPOSITADO COM SUCESSO')
            print(lista)
        else:
            sg.Popup('SENHA INVÁLIDA')
    elif window == jdeposito and evento == sg.WIN_CLOSED or evento == 'VOLTAR':
        jdeposito.hide()

#JANELA DE SAQUE
    elif window == jacesso and evento == 'SAQUE':
        jsaque = janela_saque()
        jsaque.un_hide()

    elif window == jsaque and evento == 'SALVAR':
        #Tem que esttar dentro de variável p/ a comparação
        s = valor['senha']
        lsenha = lista[posicao]['senha']
        if s == lsenha:
            valor = valor['saque']
            lista[posicao]['saldo'] -= int(valor)
            print(lista)
            sg.Popup('VALOR RETIRADO COM SUCESSO')
        else:
            sg.Popup('SENHA INVÁLIDA')

    elif window == jsaque and evento == 'VOLTAR' or evento == sg.WIN_CLOSED:
        jsaque = janela_saque()
        jsaque.hide()


