'''
script para coleta de informações ref. a DNS.
socket é nativo do s.o, geralmente desenvolvido em C. O python interpreta essa biblioteca para sua utilização
'''
import socket
#script de varredura para registros dns
domain =  input("Alvo: ")
brute = ["ns1","ns2","ns3","ns4","www","ftp","intranet","mail"] #lista de inf. ref. a registros dns.

for register in brute: #for para percorrer rodas as posições da lista brute
    DNS = register + "." + domain #variavel para receber os registros da lista brute concatenado com o domínio, formando assim o DNS
    try:
        print (DNS , ": " , socket.gethostbyname_ex(DNS)) #gethostbyname é uma função de socket que pega o ip do domínio passado
    except socket.gaierror: #caso o domínio não exista (exceção)
        pass #não exibe erro na tela e segue



