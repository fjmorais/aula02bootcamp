nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("Vocẽ digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Vocẽ não digitou nada")    
    exit()
elif nome_usuario.isspace():
    print("Vocẽ digiotu somente espaço!")
    exit()