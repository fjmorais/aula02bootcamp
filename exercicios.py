
import math

nome_aluno = '   Fabiano@gmail.com  ' 
print(type(nome_aluno))
print(type('Fabiano'))

print(nome_aluno.upper())

print(nome_aluno.lower())

print(nome_aluno.strip())

print(nome_aluno.split("@"))

#Exercicio 04

numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)

#Exercicio 10

raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2

area_do_circulo_formata = "{:.2f}".format(area_do_circulo)
print(area_do_circulo)
print(area_do_circulo_formata )
print(f"{area_do_circulo:.2f}")

#Exercicio 15
data_do_usuario = input("Insira uma data no formato dd/mm/aaaa:")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 é o: {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 é o: {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 é o: {lista_de_dia_mes_ano[2]}")
