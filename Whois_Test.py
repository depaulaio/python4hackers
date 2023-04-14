#Quem é o responsável legal sobre o domínio = WHOIS
#Em um processo de coleta de informações sobre o alvo é um tipo de pesquisa obrigatória
import whois

domain = input ("TARGET: ") #entrada do alvo
consult_whois = whois.whois(domain) #chama a função dentro da biblioteca whois para obter as informações (scanning) sobre o domínio passado.

#print (consult_whois.name) #poderetornar vazio
#print (consult_whois.fone) #pode retornar vazio
#print (consult_whois.mail) #pode retornar vazio
'''
O python NMAP permite outras vizualizações de forma mais seletiva
'''
print(consult_whois.name_servers) #consult_whois possui várias informações
print(consult_whois.status)
#print (consult_whois.yearfirst) #pode retorna false
#print (consult_whois.text) #printa todas as informações em texto puro
#print(consult_whois)
