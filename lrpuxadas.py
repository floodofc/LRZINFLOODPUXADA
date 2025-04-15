
import requests

def consulta_cep(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return response.json()

def consulta_ip(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json()

def consulta_cnpj(cnpj):
    response = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    return response.json()

def consulta_previsao(cidade, chave_api):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}")
    return response.json()

def enviar_mensagem_suporte():
    numero = input("Digite o número do WhatsApp: ")
    mensagem = input("Digite a mensagem: ")
    print("Mensagem enviada com sucesso!")

def painel():
    while True:
        print("_____________________________")
        print("█░░ █▀▀▄░█▀▄ █░█ █▀▄")
        print("█░░ █▐█▀░█▄█ ▄▀▄ █░█")
        print("▀▀▀ ▀░▀▀░▀░░ ▀░▀ ▀▀░")
        print("\nPainel de Consulta")
        print("1. Consulta de CEP")
        print("2. Consulta de IP")
        print("3. Consulta de CNPJ")
        print("4. Consulta de Previsão do Tempo")
        print("5. Enviar mensagem para suporte")
        print("6. Sair")
        print("__________________________________")
        print(" https://youtube.com/@fxbruxohanmaofc?si=xubhXYPwtp3BMGtg")
        opcao = input("Escolha uma opção>: ")

        if opcao == "1":
            cep = input("Digite o CEP: ")
            dados_cep = consulta_cep(cep)
            print(dados_cep)
        elif opcao == "2":
            ip = input("Digite o IP: ")
            dados_ip = consulta_ip(ip)
            print(dados_ip)
        elif opcao == "3":
            cnpj = input("Digite o CNPJ: ")
            dados_cnpj = consulta_cnpj(cnpj)
            print(dados_cnpj)
        elif opcao == "4":
            cidade = input("Digite a cidade: ")
            chave_api = input("Digite a chave API: ")
            dados_previsao = consulta_previsao(cidade, chave_api)
            print(dados_previsao)
        elif opcao == "5":
            enviar_mensagem_suporte()
        elif opcao == "6":
            break
        else:
            print("Opção inválida")

painel()
