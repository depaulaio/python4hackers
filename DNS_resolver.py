import dns.resolver

domain = input ("ALVO: ")
registers = ["A","AAAA","MX","NS"] #lista de registros DNS. Responsavel por campos padrão do DNS

for register in registers: #register vaiável de controle em registers (arraylist).
    result = dns.resolver.resolve(domain, register, raise_on_no_answer=False) #utiliza o metodo resolve para determinar se cada tipo de registro existe pu não. Caso não encontre a informação, não haverá perguntas (raise_on_no_answer=False).
    if result.rrset is not None: #rrset padrão do dns resolver se não for none (vazio) printa o resultado. Quando não coloca o rrset retorna o objeto armazenado na memória ram.
        print (result.rrset)