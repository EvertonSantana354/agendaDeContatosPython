from dados import agenda

def exibirMenu():
    print("====== AGENDA ======")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - Sair")

def adicionarContato(n: str, e: str, t: str):
    contato = {
         "nome": n,
        "email": e,
        "telefone": t
    }
    agenda.append(contato)
    print("Contato Adicionado!")

def exibirAgenda():
    print("CONTATOS: ")
    print("NOME      -     EMAIL        -     TELEFONE")
    print(" ")
    for contato in agenda:
        print(contato["nome"], " - ", contato["email"], " - ", contato["telefone"])
    print(" ")

def buscarContatoNaAgenda(c):
    contato = contatoExiste(c)
    if(contato != " "):
        print(contato["nome"], " - ", contato["email"], " - ", contato["telefone"])
    else:
        print("Contato não encontrado na Agenda!") 

def editarContato(c):
    contato = contatoExiste(c)
    if(contato != " "):
        print(contato["nome"], " - ", contato["email"], " - ", contato["telefone"])
        print("Qual informação deseja alterar?")
        selecao = int(input("1 - Nome / 2 - Email / 3 - Telefone "))
        if(selecao == 1):
            novoNome = str(input("Qual o novo nome do contato? ")).strip()
            contato.update({"nome": novoNome})
            print("Contato atualizado!")
        elif(selecao == 2):
            novoEmail = str(input("Qual o novo email do contato? ")).strip()
            contato.update({"nome": novoEmail})
            print("Contato atualizado!")
        elif(selecao == 3):
            novoTelefone = str(input("Qual o novo telefone do contato? ")).strip()
            contato.update({"nome": novoTelefone})
            print("Contato atualizado!")
        else:
            print("Operação inválida!")                      
    else:
        print("Contato não está na Agenda!")     

def removerContato(c):
                contato = contatoExiste(c)
                if(contato != " "):
                    print(c, "Está na Agenda!")
                    print(contato["nome"], " - ", contato["email"], " - ", contato["telefone"])
                    print("ATENÇÃO! ESSA AÇÃO É INRREVERSÍVEL")
                    print("Realmente deseja remover", contato["nome"], " da sua agenda?")
                    confirmacao = str(input("S - SIM / N - NÃO "))
                    if(confirmacao == "N"):
                        print("Exclusão cancelada")
                    else:
                        agenda.remove(contato)
                        print("Contato removido da Agenda!")
                else:
                    print("Contato não está na Agenda!")
                print(" ")

def contatoExiste(c):
    for contato in agenda:
            if contato["nome"] == c:
                return contato
            else:
                return " "
    print(" ")