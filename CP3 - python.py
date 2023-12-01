# nossa Aray paciente
paciente = []
registros_consultas = []


# função para listar os pacientes registrados
def listar_paciente(paciente):
    if not paciente:
        print("\nNão temos cadastro")
        return paciente

    print("\nLista de pacientes:")
    for nome, idade, email, celular in paciente:
        print(f"\nPaciente: {nome}, idade: {idade}, Email: {email}, Numero de contato: {celular}")


# Função para adicionar um paciente
def adicionar_pessoa(paciente, nome, idade, email, celular):
    
     pessoa = (nome, idade, email, celular)

     paciente.append(pessoa)
   
     print(f"\nPaciente {nome} cadastradado com sucesso")

     return pessoa


# função responsavel por atualizar algum paciente
def atualizar_paciente(paciente, nome, idade, email, celular):

    for i, pessoa in enumerate(paciente):
        if pessoa[0] == nome:
            paciente[i] = (pessoa[0], pessoa[1], pessoa[2], pessoa[3])
            print(f"\nPaciente atualizado.")
            return paciente
        
    print(f"Paciente não encontrado")


# Função responsavel por calcular paciente total no sisteema
def calcular_paciente_total(paciente):
    paciente_total = len(paciente)
    print(f"O total de pacientes no sistema é: {paciente_total}")


# Função para registrar uma nova consulta
def registrar_consulta(data_consulta, paciente_consulta, diagnostico_consulta, prescricao_consulta):
    consulta = {
        "data": data_consulta,
        "paciente": paciente_consulta,
        "diagnostico": diagnostico_consulta,
        "prescricao": prescricao_consulta
    }
    
    registros_consultas.append(consulta)
    print("Consulta registrada com sucesso!")
    

# função para detalhar uma consulta    
def detalhar_consulta(pacientes, nome):
    for pessoa in pacientes:
        if pessoa["paciente"] == nome:
            print(f"\nDetalhes da Consulta de {nome}:")
            print(f"\nData da Consulta: {pessoa['data']}")
            print(f"Paciente: {pessoa['paciente']}")
            print(f"Diagnóstico: {pessoa['diagnostico']}")
            print(f"Prescrição: {pessoa['prescricao']}")
            break
    else:    
        print("\nPaciente não encontrado ou não realizou nenhuma consulta")
         
    
# função para exibir os registros de consultas
def registros_de_consultas(consultas):
    consulta_total = len(consultas)
    print(f"\nO total de consultas é: {consulta_total}")
    

while True:
    print("\nMenu:") 
    print ("0 = Nome dos integrantes")
    print("1 = Adicionar paciente")
    print("2 = Listar paciente")
    print("3 = Atualizar paciente")
    print("4 = Total de pacientes registrados no sistema")
    print("5 = Registrar uma consulta")
    print("6 = Detalhar uma consulta")
    print("7 = Total de consultas registradas no sistema")
    print("8 = Sair")
    escolha = input("\nEscolha um numero de 0 a 8: ")

    if escolha == '0':
        print("João Vitor Valaitis")
        print("Gustavo Vieira Bargas")
        print("Thiago Silva Coneggin")
    elif escolha == '1':
        nome = input("Digite o nome do pessoa: ")
        idade = int(input("Digite a idade do paciente: "))
        email = input("Digite o email: ")
        celular = input("Digite o numero de contato: ")
        adicionar_pessoa(paciente, nome, idade, email, celular)
    elif escolha == '2':
        listar_paciente(paciente)
    elif escolha == '3':
        nome = input("Digite o nome do pessoa a ser atualizado: ")
        idade = int(input("Atualize a idade: "))
        email = input("Atualize o email: ")
        celular = int(input("Atualize o numero de telefone: "))
        atualizar_paciente(paciente, nome, idade, email, celular)
    elif escolha == '4':
        calcular_paciente_total(paciente)
    elif escolha == '5':
        data_consulta = input("digite a data da consulta: ")
        paciente_consulta = input("Digite o nome do paciente da consulta: ")
        diagnostico_consulta = input("Digite o diagnostico da consulta: ")
        prescricao_consulta = input("prescrição da consulta: ")
        registrar_consulta(data_consulta, paciente_consulta, diagnostico_consulta, prescricao_consulta)
    elif escolha == '6':
        nome = input("Digite o nome do paciente da consulta: ")
        detalhar_consulta(registros_consultas, nome)
    elif escolha == '7':
        registros_de_consultas(registros_consultas)   
    elif escolha == '8':
        print("\nPrograma encerrado.")
        break
    else:
        print("\nOpção inválida!")
