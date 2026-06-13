from agendaTelefonica import *

def Agenda():
    while(1):
        exibirMenu()
        acao = int(input("Escolha uma opção:"))
        match acao:
            case 1:
                nome = str(input("Insira o nome do contato:"))
                email = str(input("Insira o email do contato:"))
                telefone = str(input("Insira o telefone do contato:"))
                adicionarContato(nome, email, telefone)
            case 2:
               exibirAgenda()
            case 3:
                buscarContato = str(input("Qual contato deseja procurar? ")).strip()
                buscarContatoNaAgenda(buscarContato)                
            case 4:
                buscarContato = str(input("Qual contato deseja Atualizar? ")).strip()
                editarContato(buscarContato)
                print(" ")
            case 5:
                buscarContato = str(input("Qual contato deseja remover? ")).strip()
                removerContato(buscarContato)
            case 0:
                print("ENCERRANDO AGENDA")
                break
            case _:
                print("Opção Inválida!")
        print(" ")
    return
    
Agenda()