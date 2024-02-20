# Exemplo que causa TypeError

nome = 'Fabiano'

try: 
    resultado = len(nome)
    print(resultado)
except TypeError as e:
    print(e) #imprime mensagem de error
else:
    print("Tudo ocorreu bem")
finally:
    print("Importante é participar")
    