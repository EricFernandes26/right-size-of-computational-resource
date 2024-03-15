import boto3
import json

def perguntar_banco_dados():
    print("Qual banco de dados você está usando?")
    print("1. SQL Server")
    print("2. Oracle")
    print("3. MySQL")
    print("4. PostgreSQL")
    
    while True:
        opcao = input("Digite o número correspondente ao banco de dados: ")
        if opcao in ['1', '2', '3', '4']:
            return int(opcao)
        else:
            print("Por favor, escolha uma opção válida.")

def perguntar_servidor():
    print("\nQual tipo de servidor você está usando?")
    print("1. Servidor físico")
    print("2. Máquina virtual")
    print("3. Servidor físico que hospeda máquinas virtuais")
    
    while True:
        opcao = input("Digite o número correspondente ao tipo de servidor: ")
        if opcao in ['1', '2', '3']:
            return int(opcao)
        else:
            print("Por favor, escolha uma opção válida.")

def perguntar_recursos_servidor():
    cpu = input("Quantidade de CPU do servidor físico: ")
    ram = input("Quantidade de memória RAM do servidor físico: ")
    cpu = float(cpu.replace(',', '.'))  # Substituir vírgula por ponto decimal
    ram = float(ram.replace(',', '.'))  # Substituir vírgula por ponto decimal
    return cpu, ram

def perguntar_recursos_maquina_virtual():
    cpu = input("Quantidade de VCPU na máquina virtual: ")
    ram = input("Quantidade de memória RAM na máquina virtual: ")
    cpu = float(cpu.replace(',', '.'))  # Substituir vírgula por ponto decimal
    ram = float(ram.replace(',', '.'))  # Substituir vírgula por ponto decimal
    return cpu, ram

def perguntar_monitoramento():
    resposta = input("Houve algum período de monitoramento? (s/n): ")
    if resposta.lower() == 's':
        cpu = input("Qual a porcentagem média de uso de CPU durante o monitoramento? ")
        ram = input("Qual a porcentagem média de uso de memória RAM durante o monitoramento? ")
        cpu = float(cpu.replace(',', '.'))  # Substituir vírgula por ponto decimal
        ram = float(ram.replace(',', '.'))  # Substituir vírgula por ponto decimal
        return cpu, ram
    elif resposta.lower() == 'n':
        return None
    else:
        print("Por favor, responda com 's' para sim ou 'n' para não.")
        return perguntar_monitoramento()

def gerar_frase(opcao_bd, opcao_servidor, recursos_servidor=None, recursos_vm=None, monitoramento=None):
    frase = "Um cliente está usando um "
    
    if opcao_bd == 1:
        frase += "SQL Server."
    elif opcao_bd == 2:
        frase += "Oracle."
    elif opcao_bd == 3:
        frase += "MySQL."
    elif opcao_bd == 4:
        frase += "PostgreSQL."
    
    if opcao_servidor == 1:
        frase += " Em um servidor físico com "
        frase += f"{recursos_servidor[0]} CPU(s) e {recursos_servidor[1]} GB de RAM."
    elif opcao_servidor == 2:
        frase += " Em uma máquina virtual com "
        frase += f"{recursos_vm[0]} VCPU(s) e {recursos_vm[1]} GB de RAM."
    elif opcao_servidor == 3:
        frase += " Em um servidor físico que hospeda máquinas virtuais."
        frase += f" O servidor físico possui {recursos_servidor[0]} CPU(s) e {recursos_servidor[1]} GB de RAM."
        frase += f" A máquina virtual possui {recursos_vm[0]} VCPU(s) e {recursos_vm[1]} GB de RAM."
    
    if monitoramento:
        frase += f" Durante o monitoramento, a porcentagem média de uso de CPU foi de {monitoramento[0]}% e de RAM foi de {monitoramento[1]}%. Qual seria a melhor opção de máquina disponível na AWS para replicar esse ambiente?"
    else:
        frase += " Não foi obtido nenhum período de monitoramento registrado. Qual seria a melhor opção de máquina disponível na AWS para replicar esse ambiente?"
    
    return frase

def main():
    opcao_bd = perguntar_banco_dados()
    opcao_servidor = perguntar_servidor()
    
    recursos_servidor = None
    recursos_vm = None
    monitoramento = None
    
    if opcao_servidor == 1:
        recursos_servidor = perguntar_recursos_servidor()
    elif opcao_servidor == 2:
        recursos_vm = perguntar_recursos_maquina_virtual()
    elif opcao_servidor == 3:
        recursos_servidor = perguntar_recursos_servidor()
        print("\nAgora, vamos especificar os recursos da máquina virtual.")
        recursos_vm = perguntar_recursos_maquina_virtual()
    
    monitoramento = perguntar_monitoramento()
    
    frase = gerar_frase(opcao_bd, opcao_servidor, recursos_servidor, recursos_vm, monitoramento)
    print(frase)
    
    # Integração com Bedrock da AWS
    brt = boto3.client(service_name='bedrock-runtime')

    body = json.dumps({
        "prompt": f"\n\nHuman: {frase}\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })

    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    print(response_body.get('completion'))

if __name__ == "__main__":
    main()
