#----------------------------------------------------------------------------
#CRIAÇÃO DA FUNÇÃO MENU
#import json
def menu():
  print(''' 
  Bem vindo ao Petshop Au-Miau!
  Escolha uma das opções abaixo:

  1. Usuário
  2. Animal de estimação
  3. Agendamentos
  0. Sair
  ''')

def menu1():
  print('''
  Escolha uma das opções abaixo:

  1. Inserir usuário
  2. Visualizar usuários cadastrados
  3. Alterar usuários cadastrados
  4. Excluir usuários cadastrados
  0. Sair
  ''')

def menu2():
  print('''
  Escolha uma das opções abaixo:

  1. Inserir informações sobre animal
  2. Visualizar animais cadastrados
  3. Alterar informações dos animais
  4. Excluir animal cadastrado
  0. Sair
  ''')

def menu3():
  print('''
  Escolha uma das opções abaixo:

  1. Agendar serviço
  2. Visualizar Agendamentos
  3. Editar Agendamentos
  4. Excluir Agendamentos
  0. Sair
  ''')

#----------------------------------------------------------------------------

#CRIAÇÃO DA FUNÇÃO QUE CADASTRA OS USUÁRIOS
def cadastro(usuarios):
  nome= input("Digite seu nome completo: ")
  contato= input("Digite seu telefone para contato: ")
  cpf= input("Digite seu CPF: ")
  endereco= input("Digite seu endereço: ")
  id = input("Digite seu número de identificação:")
  usuarios.append((nome, contato, cpf, endereco, id))



#CRIAÇÃO DA FUNÇÃO QUE EXIBE OS USUÁRIOS
def exibir(usuarios):
  if len(usuarios) == 0:
    print('Nenhuma pessoa cadastrada!')
  else:
    for pessoa in usuarios:
      nome, contato, cpf, endereco, id = pessoa
      print(f'nome: {nome}, contato: {contato}, CPF: {cpf}, endereço: {endereco}, Id: {id}')

#ALTERAR USUÁRIOS
def alterar(usuarios):
  identificador_id= input('Digite seu ID para confirmar quais informações desejam ser alteradas: ')
  for pessoa in usuarios:
    nome, contato, cpf, endereco, id = pessoa
    if id == identificador_id:
      print(f'Nome: {nome}, Contato: {contato}, CPF: {cpf}, Endereço: {endereco}, Id: {id}')

      novonome = input('Digite o novo nome:')
      novocontato = input('Digite o novo contato:')
      novocontato=int(novocontato)
      novocpf = input('Digite um novo CPF: ')
      novocpf=int(novocpf)
      novoendereco = input('Digite um novo endereço: ')
      #novoendereco=int(novoendereco)
      confirma = input('Para alterar digite 1, para negar a alteração digite 0: ')
      confirma = int(confirma)
      if confirma == 1:
        usuarios[usuarios.index(pessoa)] = novonome, novocontato, novocpf, novoendereco, id
        print(f'Nome: {novonome}, Contato: {novocontato}, CPF: {novocpf}, Endereço: {novoendereco}, Id: {id}')
      break
  else:
      print(f'Pessoa com o Id {identificador_id} não encontrada')

#EXCLUIR USUÁRIO
def excluir(usuarios):
  identificador_desejado = input('Id?')
  for pessoa in usuarios:
    nome, contato, cpf, endereco, id = pessoa
    if id == identificador_desejado:
      print(f'nome: {nome}, contato: {contato}, CPF: {cpf}, endereço: {endereco}, Id: {id}')
      excluir = input('Para excluir digite 1, para negar digite 0: ')
      excluir=int(excluir)
      if excluir == 1:
        del usuarios[usuarios.index(pessoa)]
        print(f'Pessoa com id {identificador_desejado} excluida com sucesso!')
        break
    else:
      print(f'Pessoa com id {identificador_desejado} não encontrada')

#----------------------------------------------------------------------------

#CRIAÇÃO DA FUNÇÃO QUE CADASTRA ANIMAL
def cadastro2(animal):
  nome= input("Digite o nome do animal: ")
  raca= input("Qual a raça do seu animal?")
  idade= input("Quantos anos tem seu animal? ")
  peso= input("Quantos quilos seu animal tem?")
  id_a = input("Digite o número de identificação do animal: ")
  animal.append((nome, raca, idade, peso, id_a))



#CRIAÇÃO DA FUNÇÃO QUE EXIBE OS ANIMAIS
def exibir2(animal):
  if len(animal) == 0:
    print('Nenhuma animal cadastrado!')
  else:
    for a in animal:
      nome, raca, idade, peso, id_a = a
      print(f'nome: {nome}, raça: {raca}, idade: {idade}, peso: {peso}, Id: {id_a}')

#ALTERAR ANIMAL
def alterar2(animal):
  identificador_ida= input('Digite seu ID para confirmar qual animal deve ter suas informações alteradas: ')
  for a in animal:
    nome, raca, idade, peso, id_a = a
    if id_a == identificador_ida:
      print(f'nome: {nome}, raça: {raca}, idade: {idade}, peso: {peso}, Id: {id_a}')

      novonome = input('Digite o novo nome do seu animal:')
      novaraca = input('Digite a nova raça do seu animal:')
      novaidade = input('Digite uma nova idade: ')
      novaidade=int(novaidade)
      novopeso = input('Digite um novo peso: ')
      novopeso=int(novopeso)
      confirma = input('Para alterar digite 1, para negar a alteração digite 0: ')
      confirma = int(confirma)
      if confirma == 1:
        animal[animal.index(a)] = novonome, novaraca, novaidade, novopeso, id_a
        print(f'nome: {nome}, raça: {raca}, idade: {idade}, peso: {peso}, Id: {id_a}')
      break
  else:
      print(f'Pessoa com o Id {identificador_ida} não encontrada')

#EXCLUIR ANIMAL
def excluir2(animal):
  identificador_a = input('Id?')
  for a in animal:
    nome, raca, idade, peso, id_a = a
    if id_a == identificador_a:
      print(f'nome: {nome}, raça: {raca}, idade: {idade}, peso: {peso}, Id: {id_a}')
      excluir = input('Para excluir digite 1, para negar digite 0: ')
      excluir=int(excluir)
      if excluir == 1:
        del animal[animal.index(a)]
        print(f'Animal com id {identificador_a} excluido com sucesso!')
      break
    else:
      print(f'Animal com id {identificador_a} não encontrado')

#----------------------------------------------------------------------------
#FUNÇÃO QUE REALIZE AGENDAMENTO (entidade de negócio)
#CRIAÇÃO DA FUNÇÃO QUE MOSTRA OS SERVIÇOS DISPONIVEIS NO PETSHOP
def inserir(agenda, usuarios, animal):
  servicos=[]
  soma=0
  print('''
  Serviços prestados pelo estabelecimento:

  1.Serviço de Banho / R$ 70
  2.Serviço de Tosa / R$ 55
  3.Escovar os dentes/ R$ 15
  4.Serviço de Corte de unha / R$ 15
   ''')
  escolha=input("Digite qual serviço deseja realizar: ")
  escolha.upper()
  while escolha != "":

    if escolha == '1':
      servico = 'Serviço de Banho'
      servicos.append(servico)
      soma=soma+70
    elif escolha == '2':
      servico = 'Serviço de Tosa'
      servicos.append(servico)
      soma=soma+55
    elif escolha == '3':
      servico = 'Escovar os dentes'
      servicos.append(servico)
      soma=soma+15
    elif escolha == '4':
      servico = 'Serviço de Corte de unha'
      servicos.append(servico)
      soma=soma+15
    else:
      print('Serviço indisponivel')
    escolha=input("Digite qual serviço deseja realizar (Deixe em branco para parar): ")
    escolha.upper()

  data = input('Escolha a data que deseja agendar: ')
  hora = input('Escolha a hora que deseja agendar: ')
  dono_id= input("Digite o Id do dono do animal: ")
  animal_id= input("Digite o Id do animal: ")
  valor_total=soma
  servicos_agendados=servicos
  dono= ""
  ani=""


  for pessoa in usuarios:
    nome, contato, cpf, endereco, id = pessoa
    if id == dono_id:
      dono=pessoa
  for a in animal:
    nome, raca, idade, peso, id_a = a
    if id_a == animal_id:
      ani=a
  n_agendamento= len(agenda)+1
  agenda.append((data, hora, dono, ani, valor_total, servicos_agendados, n_agendamento))

  print(f'Data: {data}, Hora: {hora}, Serviços Agendados:{servicos_agendados}, Informações do Dono: {dono}, Informações do animal: {ani}, Valor total: {valor_total}, numero de agendamento: {n_agendamento}')

#CRIAÇÃO DA FUNÇÃO QUE EXIBE OS AGENDAMENTOS
def exibir3(agenda, usuarios, animal):
  if len(agenda) == 0:
    print('Nenhum agendamento realizado!')
  else:
    for i in agenda:
      data, hora, dono, ani, valor_total, servicos_agendados, n_agendamento = i
      print(f'Data: {data}, Hora: {hora}, Serviços Agendados:{servicos_agendados}, Informações do Dono: {dono}, Informações do animal: {ani}, Valor total:{valor_total}, numero de agendamento: {n_agendamento}')

#ALTERAR AGENDAMENTOS
def alterar3(agenda, usuarios, animal):

  nservicos=[]
  nsoma=0
  n_agenda= input('Digite o seu número de agendamento para confirmar qual agendamento deseja ser alterado: ')
  n_agenda=int(n_agenda)
  for i in agenda:
    data, hora, dono, ani, valor_total, servicos_agendados, n_agendamento = i
    if n_agenda == n_agendamento:
      print(f'Data: {data}, Hora: {hora}, Serviços Agendados:{servicos_agendados}, Informações do Dono: {dono}, Informações do animal: {ani}, Valor total:{valor_total}, numero de agendamento: {n_agendamento}')
      ndata = input('Digite uma nova data: ')
      nhora = input('Digite um novo horário:')

#pedir novamente os serviços e os usuários
      print('''
      Serviços prestados pelo estabelecimento:

      1.Serviço de Banho / R$ 70
      2.Serviço de Tosa / R$ 55
      3.Escovar os dentes/ R$ 15
      4.Serviço de Corte de unha / R$ 15
      ''')
      novaescolha=input("Atualize qual serviço deseja realizar: ")
      novaescolha.upper()
      while novaescolha != "":

        if novaescolha == '1':
          nservico = 'Serviço de Banho'
          nservicos.append(nservico)
          nsoma=nsoma+70
        elif novaescolha == '2':
          nservico = 'Serviço de Tosa'
          nservicos.append(nservico)
          nsoma=nsoma+55
        elif novaescolha == '3':
          nservico = 'Escovar os dentes'
          nservicos.append(nservico)
          nsoma=nsoma+15
        elif novaescolha == '4':
          nservico = 'Serviço de Corte de unha'
          nservicos.append(nservico)
          nsoma=nsoma+15
        else:
          print('Serviço indisponivel')
        novaescolha=input("Atualize qual serviço deseja realizar (Deixe em branco para parar): ")
        novaescolha.upper()

      ndono_id= input("Digite o novo Id do dono do animal: ")
      nanimal_id= input("Digite o novo Id do animal: ")
      nvalor_total=nsoma
      nservicos_agendados=nservicos
      nn_agendamento= n_agendamento
      ndono= ""
      nani=""


      for pessoa in usuarios:
        nome, contato, cpf, endereco, id = pessoa
        if id == ndono_id:
          ndono=pessoa
      for a in animal:
        nome, raca, idade, peso, id_a = a
        if id_a == nanimal_id:
          nani=a

  #confirmação das novas informações
      confirma = input('Para alterar digite 1, para negar a alteração digite 0: ')
      confirma = int(confirma)
      if confirma == 1:
        agenda[agenda.index(i)] = ndata, nhora, ndono, nani, nvalor_total, nservicos_agendados, nn_agendamento
      print(f'Data: {ndata}, Hora: {nhora}, Serviços Agendados:{nservicos_agendados}, Informações do Dono: {ndono}, Informações do animal: {nani}, Valor total:{nvalor_total}, numero de agendamento: {nn_agendamento}')
      break
    else:
      print(f'Agendamento de número {n_agenda} não encontrado')


#EXCLUIR AGENDAMENTOS
def excluir3(agenda):
  agendamento_n = input('Digite o número do agendamento que deseja excluir: ')
  agendamento_n=int(agendamento_n)
  for i in agenda:
    data, hora, dono, ani, valor_total, servicos_agendados, n_agendamento = i
    if agendamento_n == n_agendamento:
      print(f'Data: {data}, Hora: {hora}, Serviços Agendados:{servicos_agendados}, Informações do Dono: {dono}, Informações do animal: {ani}, Valor total:{valor_total}, numero de agendamento: {n_agendamento}')
      excluir = input('Para excluir digite 1, para negar digite 0: ')
      excluir=int(excluir)
      if excluir == 1:
        del agenda[agenda.index(i)]
        print(f'O Agendamento de número {n_agendamento} foi excluido com sucesso!')
      break
  else:
    print(f'Agendamento de número {n_agendamento} não encontrado')



#----------------------------------------------------------------------------

#CRIAÇÃO DA FUNÇÃO QUE CHAMA A FUNÇÃO MENU
def main():
  usuarios= []
  animal= []
  agenda= []
  opcao = 1
  while opcao != 0:
    menu()
    opcao =input('Escolha uma das opções que deseja realizar: ')
#------------------------------------

#ABIR MENU USUARIOS
    if opcao == "1":
      usuarios= []
      opcao1 = 1
      while opcao1 != 0:
        menu1()
        opcao1 =input('Escolha uma das opções que deseja realizar em "Usuário": ')
        opcao1 = int(opcao1)
        if opcao1 == 1:
          cadastro(usuarios)
        elif opcao1 == 2:
          exibir(usuarios)
        elif opcao1 == 3:
          alterar(usuarios)
        elif opcao1 == 4:
          excluir(usuarios)
        elif opcao1 == 0:
          break
        else:
          print('Opção inválida')

#------------------------------------

#ABIR MENU ANIMAL
    elif opcao == "2":
        animal= []
        opcao2 = 1
        while opcao2 != 0:
          menu2()
          opcao2 =input('Escolha uma das opções que deseja realizar em "Animal de estimação": ')
          opcao2 = int(opcao2)
          if opcao2 == 1:
            cadastro2(animal)
          elif opcao2 == 2:
            exibir2(animal)
          elif opcao2 == 3:
           alterar2(animal)
          elif opcao2 == 4:
            excluir2(animal)
          elif opcao2 == 0:
            break
          else:
            print('Opção inválida')

#ABIR MENU AGENDAMENTOS

    elif opcao == "3":
      agenda= []
      opcao3 = 1
      while opcao3!= 0:
        menu3()
        opcao3 =input('Escolha uma das opções que deseja realizar em "Agendamentos": ')
        opcao3 = int(opcao3)
        if opcao3 == 1:
          inserir(agenda, usuarios, animal)
        elif opcao3 == 2:
          exibir3(agenda, usuarios, animal)
        elif opcao3 == 3:
          alterar3(agenda, usuarios, animal)
        elif opcao3 == 4:
          excluir3(agenda)
        elif opcao3 == 0:
          break
        else:
          print('Opção inválida')
    elif opcao == "0":
      print('Programa encerrado')
      break
    else:
      print('Opção inválida')


main()

# #JSON (NÃO SDEU CERTO)
#carregar, salvar, um json para cada entidade );(NÃO SDEU CERTO)

# import json

# def salvar_dados (usuarios, filename="dados.json"):
#   with open(filename, 'w') as f:
#     json.dump(usuarios, f)


# def carregar_dados (filename="dados.json"):
#   try:
#     with open(filename, 'r') as f:
#       return json.load(f)

#   except FileNotFoundError:
#     return []


# #CRIAÇÃO DA FUNÇÃO QUE CHAMA A FUNÇÃO MENU
# def main():
#   usuarios= carregar_dados()
#   animal= carregar_dados()
#   agenda= carregar_dados()
#   opcao = 1
#   while opcao != 0:
#     menu()
#     opcao =input('Escolha uma das opções que deseja realizar: ')
# #------------------------------------

#ABIR MENU USUARIOS
#     if opcao == "1":
#       usuarios= []
#       opcao1 = 1
#       while opcao1 != 0:
#         menu1()
#         opcao1 =input('Escolha uma das opções que deseja realizar em "Usuário": ')
#         opcao1 = int(opcao1)
#         if opcao1 == 1:
#           cadastro(usuarios)
#         elif opcao1 == 2:
#           exibir(usuarios)
#         elif opcao1 == 3:
#           alterar(usuarios)
#         elif opcao1 == 4:
#           excluir(usuarios)
#         elif opcao1 == 0:
#           salvar_dados(usuarios)
#           break
#         else:
#           print('Opção inválida')

# #------------------------------------

# #ABIR MENU ANIMAL
#     elif opcao == "2":
#         animal= []
#         opcao2 = 1
#         while opcao2 != 0:
#           menu2()
#           opcao2 =input('Escolha uma das opções que deseja realizar em "Animal de estimação": ')
#           opcao2 = int(opcao2)
#           if opcao2 == 1:
#             cadastro2(animal)
#           elif opcao2 == 2:
#             exibir2(animal)
#           elif opcao2 == 3:
#            alterar2(animal)
#           elif opcao2 == 4:
#             excluir2(animal)
#           elif opcao2 == 0:
#             salvar_dados(animal)
#             break
#           else:
#             print('Opção inválida')

# #ABIR MENU AGENDAMENTOS

#     elif opcao == "3":
#       agenda= []
#       opcao3 = 1
#       while opcao3!= 0:
#         menu3()
#         opcao3 =input('Escolha uma das opções que deseja realizar em "Agendamentos": ')
#         opcao3 = int(opcao3)
#         if opcao3 == 1:
#           inserir(agenda, usuarios, animal)
#         elif opcao3 == 2:
#           exibir3(agenda, usuarios, animal)
#         elif opcao3 == 3:
#           alterar3(agenda, usuarios, animal)
#         elif opcao3 == 4:
#           excluir3(agenda)
#         elif opcao3 == 0:
#           salvar_dados(agenda)''
#           break
#         else:
#           print('Opção inválida')
#     elif opcao == "0":
#       print('Programa encerrado')
#       break
#     else:
#       print('Opção inválida')


# if __name__ == '__main__':
#   main_1()
