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
print("çalsdjfalsdj")
listanumeros = list(range(1, int(maximo)))

arrayprimos = []
arrayTrueFalse = []

index = 0
while index < len(listanumeros) - 1:
    status = True
    i = 2
    while i < listanumeros[index]:  # Dividir até o número menor que ele
        if listanumeros[index] % math.sqrt(i) == 0: #Só preciso testar o resto da divisão até a raiz do próprio número
            status = False
            break  # Já podemos sair, porque ele não é primo
        else:
            status = True
            print("aslçdkjf")
        i = i + 1
    if status == True:
        # arrayprimos.append(listanumeros[index])
        print("desgraça")
    index += 1
#
# print("T", arrayTrueFalse)
# print("T")
# # print("A lista de números primos é:", listaprimos)


#Cross-off:
