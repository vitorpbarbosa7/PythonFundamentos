import math
try:
    maximo = int(input("Digite o valor superior: \n"))
except ValueError as v:
    print("Você não digitou um número inteiro", v)
except NameError as n:
    print("Você não digitou nenhum número", n)
finally:
    print("Serão calculados os números primos até o limite superior de: ", (maximo))

# print(isinstance(maximo, int)) #Como checar se o objeto é de tal tipo
listanumeros = list(range(2, int(maximo)))
listaprimos = []
listaTrueFalse = [False, False]

index = 0
while index < len(listanumeros) - 1:
    status = True
    i = 2
    while i < listanumeros[index]:  # Dividir até o número menor que ele
        if listanumeros[index] % i == 0: #Só preciso testar o resto da divisão até a raiz do próprio número
            status = False
            listaTrueFalse.append(status)
            break  # Já podemos sair, porque ele não é primo
        else:
            status = True
        i = i + 1
    if status == True:
        listaprimos.append(listanumeros[index])
        listaTrueFalse.append(status)
    index += 1

print("A lista de números primos é:", listaprimos)
print("Lista de True/False:", listaTrueFalse)

#Cross-off: