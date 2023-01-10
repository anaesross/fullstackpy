# permite escrever um comentário
print('Imprimir texto da tela')
#função print, utilizada parae exibir na tela - a função recebe argumentos separados por ,  EX:
print(12, 24) #argumentos não nomeados
print(14, 78) #argumentos não nomeados

# argumentos com separador
print(12, 84, sep='-')
print(12, 24, sep="--")

#\r\n  = return line feed = CRLF  - quebrar linha 

#Tipagem forte e dinâmica
#string
print("uma string")
print('uma string')
print("Alo \"escape")

#int
print(0)
print(1)

#float (utiliza . ponto para separar as casas)
print(1.2)
print(-5.8)

#função (classe type) type mostra o tipo que o python inferiu ao valor
print(type("Alo Mundão!"))
print(type(0))
print(type(5.3), type(-1.1))

#boolean  true or false 
print(10 == 10) #True
print(10 == 11) #False
print(type(10 == 10), type(True), type(False))

