#Enumeração de usuários dentro de um servidor SMTP (Simple Mail Transfer Protocol), protocolo para envio de e-mail.
#Encontra usuários dentro de um servidor SMTP, através de um bruteforce.
#A maioria dos servidores já possuem segurança para esse tipo de brecha.

import socket
users = ["contato","comercial","financeiro","vendas","atendimento","sac","root","trial"] #lista para bruteforce.
target = input("TARGET: ")
for user in users:#for para percorrer os usuários por meio de bruteforce
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Cria socket para conectar ao servidor SMTP. Sock é uma variável para encurtar as funções chamadas da biblioteca
    sock.connect((target,25))#conecta o socket criado a porta do servidor SMTP (25 por padrão)
    sock.recv(1024)#recebe banner do servidor. Caso consiga realizar a conexão o banner do servidor é recebido.
    sock.send("VRFY" + user + "\n")#Envia via send (do comando objeto SOCK e VRFY para verificar se o usuário existe. Caracteristicas VRFY e usuário.... VRFY contato, VRFY comercial....)
    smtp_result = sock.recv(1024)#Recebe 1024 bytes de entrada, sendo cada divisao deles uma resposta diferente
    sock.close() #Finaliza o socket criado
    if "252" in smtp_result: #Faz a verificação do resultado.
        print (user + "--> Válido!")
    elif "550" in smtp_result:
        print (user+ "---> Usuário Inválido!")
    elif "503" in smtp_result:
        print ("Servidor requer autenticação")
        break
    elif "500" in smtp_result:
        print ("Comando VRFY não suportado pelo servidor")
        break
    else:
        print ("Resposta ao servidor: ", smtp_result)
