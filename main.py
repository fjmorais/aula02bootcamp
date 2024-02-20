# Exemplo que causa TypeError

#nome = 'Fabiano'

#try: 
#    resultado = len(nome)
#    print(resultado)
#except TypeError as e:
#    print(e) #imprime mensagem de error
#else:
#    print("Tudo ocorreu bem")
#finally:
#    print("Importante é participar")

#numero = int(input("Inserir um núemro:"))
#if isinstance(numero,int):
#    print("A variável é um inteiro.")
#else:
#    print("A variável não é um inteiro")

idade = 18

if idade < 18:
    print("Não pode dirigir")
elif idade == 18:
    print("Processo de estudos")    
else:
    print("Direção permitida")