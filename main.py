agenda = [
    {
     "nome":"everton",
     "email":"andradeeverton354@gmail.com",
     "telefone":"84991525022"
     }
]

def Agenda():
    while(1):
        print("====== AGENDA ======")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Editar contato")
        print("5 - Excluir contato")
        print("0 - Sair")
        acao = int(input("Escolha uma opção:"))
        match acao:
            case 1:
                nome = str(input("Insira o nome do contato:"))
                email = str(input("Insira o email do contato:"))
                telefone = str(input("Insira o telefone do contato:"))
                contato = {
                    "nome": nome,
                    "email": email,
                    "telefone": telefone
                }
                agenda.append(contato)
                print("Contato Adicionado!")
            case 2:
                print("CONTATOS: ")
                print("NOME      -     EMAIL        -     TELEFONE")
                print(" ")
                for contato in agenda:
                    print(contato["nome"], " - ", contato["email"], " - ", contato["telefone"])
                    print(" ")
            case 3:
                buscarContato = str(input("Qual contato deseja procurar? ")).strip()
                print(" ")
                for contato in agenda:
                    if contato["nome"] == buscarContato:
                        print(buscarContato, "Está na Agenda!")
                        print(contato["nome"], " - ", contato["email"], " - ", contato["telefone"])
                    else:
                        print("Contato não está na Agenda!")
                    print(" ")
            case 4:
                buscarContato = str(input("Qual contato deseja Atualizar? ")).strip()
                for contato in agenda:
                    if contato["nome"] == buscarContato:
                        print(contato)
                        print(buscarContato, "Está na Agenda!")
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
                    print(" ")
            case 5:
                buscarContato = str(input("Qual contato deseja remover? ")).strip()
                for contato in agenda:
                    if contato["nome"] == buscarContato:
                        print(buscarContato, "Está na Agenda!")
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
            case 0:
                print("ENCERRANDO AGENDA")
                break
            case _:
                print("Opção Inválida!")
        print(" ")
    return
    
Agenda()