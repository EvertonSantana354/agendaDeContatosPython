import csv
from pathlib import Path
agenda = []

def criarAgendaTelefonica():
    agendaTelefonica = Path("contatos.csv")
    if agendaTelefonica.is_file():
        carregarContatos()
    else:
        print("Criando arquivo de contatos da Agenda Telefonica")
        agendaTelefonica = open("contatos.csv", "x", encoding="utf-8")
        agendaTelefonica.close()

def carregarContatos():
     with open("contatos.csv","r") as f:
        csvReader = csv.reader(f,delimiter=",")
        for linha in csvReader:
             agenda.append(linha)

def exibirMenu():
    print("====== AGENDA ======")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - Sair")

def validarTelefone(t: str):
    if len(t) != 11:
          return False
    for digito in t:
          if not(digito.isnumeric()):
            return False
    return True

def adicionarContato(n: str, e: str, t: str):
    contato = [n,e,t]
    with open("contatos.csv","a") as f:
         csvWriter =  csv.writer(f, delimiter=",")
         csvWriter.writerow(contato)
    agenda.append(contato)
    print("Contato Adicionado!")

def exibirAgenda():
    if(len(agenda) == 0):
        print("Agenda está vazia")
        return
    print("CONTATOS: ")
    print("NOME      -     EMAIL        -     TELEFONE")
    print(" ")
    for contato in agenda:
        print(contato[0], " ", contato[1], " ", contato[2], "\n")
    print("\n")

def buscarContatoNaAgenda(c):
    contato = contatoExiste(c)
    if(contato != None):
        print(contato[0], " - ", contato[1], " - ", contato[2])
    else:
        print("Contato não encontrado na Agenda!") 

def editarContato(c):
    contato = contatoExiste(c)
    if(contato != None):
        print(contato[0], " - ", contato[1], " - ", contato[2])
        print("Qual informação deseja alterar?")
        selecao = int(input("1 - Nome / 2 - Email / 3 - Telefone "))
        if(selecao == 1):
            novoNome = str(input("Qual o novo nome do contato? ")).strip()
            contato[0] = novoNome
            print("Contato atualizado!")
        elif(selecao == 2):
            novoEmail = str(input("Qual o novo email do contato? ")).strip()
            contato[1] = novoEmail
            print("Contato atualizado!")
        elif(selecao == 3):
            novoTelefone = str(input("Qual o novo telefone do contato? ")).strip()
            contato[2] = novoTelefone
            print("Contato atualizado!")
        else:
            print("Operação inválida!")                      
    else:
        print("Contato não está na Agenda!")     

def removerContato(c):
    contato = contatoExiste(c)
    if(contato != None):
        print(c, "Está na Agenda!")
        print(contato[0], " - ", contato[1], " - ", contato[2])
        print("ATENÇÃO! ESSA AÇÃO É INRREVERSÍVEL")
        print("Realmente deseja remover", contato[0], " da sua agenda?")
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
            if contato[0] == c:
                return contato
            else:
                return None