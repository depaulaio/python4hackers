#script de varredura para registros dns utilizando arquivo (.txt) para maximizar as possibilidades e facilitar a leitura do código
import socket

domain = input ("ALVO: ")
with open ("bruteDNS.txt", "r") as file: #nome para ref. o arquivo dentro do código 'file'. Utilizando o 'r' para realizar a leitura do arquivo.
    bruteDNS = file.readlines() #utilizando a função readline para leitura das linhas do arquivo. bruteDNS será equivalente a uma linha de registro no arquivo.
for register in bruteDNS: #percorrendo todos os registro passados na linha do arquivo bruteDNS
    DNS = register.strip("\n") + "." + domain
    try:
        print (DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass