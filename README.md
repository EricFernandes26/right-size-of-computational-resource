# right-size-of-computational-resource

# Descrição do Código
O código em questão é um script Python que interage com o usuário para obter informações sobre o ambiente de banco de dados e servidor utilizado por um cliente. Com base nessas informações, ele gera uma frase descrevendo o ambiente e, em seguida, faz uma solicitação para um serviço de integração com Bedrock da AWS para gerar uma resposta automatizada.

## O script segue as seguintes etapas:

Pergunta ao usuário sobre o banco de dados utilizado, oferecendo opções como SQL Server, Oracle, MySQL e PostgreSQL.  

Pergunta ao usuário sobre o tipo de servidor, incluindo opções como servidor físico, máquina virtual e servidor físico que hospeda máquinas virtuais.  

Com base na resposta do usuário, solicita mais informações sobre os recursos do servidor físico ou da máquina virtual, se aplicável.  

Pergunta se houve algum período de monitoramento e, se sim, solicita informações sobre o uso médio de CPU e RAM durante esse período.  

Com todas as informações coletadas, gera uma frase descritiva do ambiente.  

Integra-se com o serviço Bedrock da AWS para gerar uma resposta automatizada com base na frase gerada.  



## Requisitos
* Python 3.x instalado
* Conta na AWS com acesso ao serviço Bedrock

## Instalação
* Clone ou faça o download deste repositório.
* Certifique-se de ter configurado corretamente suas credenciais da AWS, preferencialmente utilizando o AWS CLI.
* Instale as dependências do Python executando o seguinte comando no terminal: pip install boto3

## Como Executar
* Navegue até o diretório onde o script está localizado.
* Execute o script  exe.bat
* Siga as instruções fornecidas pelo script para responder às perguntas sobre o ambiente de banco de dados e servidor.
* Aguarde a resposta gerada automaticamente pelo serviço Bedrock da AWS.

## Notas
O Script exe.bat tem como padrao o diretorio "C:\Users\Administrator\Desktop\right-size-of-computational-resource\app.py" altere para executar o script em sua maquina.    
Certifique-se de ter configurado corretamente suas permissões na AWS para acessar o serviço Bedrock.  
Este script interage com o usuário por meio da linha de comando. Certifique-se de executá-lo em um ambiente compatível com a entrada do terminal.  

## Output do script
![image](https://github.com/EricFernandes26/right-size-of-computational-resource/assets/83287307/10fae232-34b8-4842-ac2c-d4a19524ba8c)  

![image](https://github.com/EricFernandes26/right-size-of-computational-resource/assets/83287307/1f24112d-fc6d-4828-9aee-be3508e6dacb)  

![image](https://github.com/EricFernandes26/right-size-of-computational-resource/assets/83287307/50b4049a-16c4-4e61-be16-2802d2657559)  



