import dns.resolver

domain_target = input("TARGET: ") #alvo dns a ser verificado

result = dns.resolver.resolve(domain_target, "A") #padrão para chamar a classe resolve dentro da biblioteca resolver, passando o alvo e o registro "A".
for ipval in result: #valor do ip percorrido no result
    print("IP: ", ipval.to_text()) #printa somente quando encontra o ip e converte para texto
    iptarget = ipval.to_text() #passado para variável
#-------------------------------------------------------------------------
'''
CNAME pega o subdominio e verifica qual o real subdominio. ex. google.com não tem subdominio, logo resulta em erro.
Contrário de mail.google.com, por exemplo, onde será retornada alguma informação.
'''
print ("-------")

try: #trata possível erro no busca pelo CNAME
    result = dns.resolver.resolve(domain_target, "CNAME")
    for cnameval in result:
        print ("CNAME: ", cnameval.target) #utiliza target
except: #ignora o erro
    pass

#-------------------------------------------------------------------------
print ("-------")

result = dns.resolver.resolve(domain_target, "AAAA")
for val in result:
    print ("AAAA: ", ipval.to_text())
#-------------------------------------------------------------------------
'''
Para obtençao do PTR é necessário o IP, não é possível obter o PTR somente com o domínio.
Por isso se utilizou a variável iptarget dentro do dns.resolver.resolve
'''
print ("-------")

try:
    result = dns.resolver.resolve(iptarget + "in-addr.arpa", "PTR") #utiliza o ip alvo com o dns.resolver.resolve para obter o PTR.
    for val in result:
        print ("PTR: ",val.to_text())
except: #ignora o erro
    pass
#-------------------------------------------------------------------------
print ("-------")

result = dns.resolver.resolve(domain_target, "NS")
for val in result:
    print("NS: ", val.to_text())
#-------------------------------------------------------------------------
print ("-------")

results = dns.resolver.resolve(domain_target, "MX")
for exdata in results:
    print("MX: ", exdata.to_text())
#-------------------------------------------------------------------------
print ("-------")

result = dns.resolver.resolve(domain_target, "SOA")
for val in result:
    print("SOA: ", val.to_text())
#-------------------------------------------------------------------------
print ("-------")

try:
    result = dns.resolver.resolve(domain_target, "TXT")
    for val in result:
        print("TXT: ", val.to_text())
except:
    pass
#-------------------------------------------------------------------------
print ("-------")



