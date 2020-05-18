# numero = random.randint(0,len(dataset)-1)
# print(numero)
# palavra = dataset[numero]
palavra = 'banana'
print(palavra)

# Trabalhar em cima dos indices:
list(enumerate(palavra))

indices = []
letras = []
for index, letra in enumerate(palavra):
    indices.append(index)
    letras.append(letra)
    # print(index, letra)

print(indices, letras)

tentativas = 7
acertos = 0
tent = 0
status = False  # Não adivinhou nada
# Inicializando a lista vazia:
dinamica = [None] * len(letras)
# print(dinamica)
# print(len(dinamica))

#deletarindices
delindex = []
while status == False:
    letra = input("Digite uma letra \n")
    # Percorrer os indices:
    for indice in indices:
        if letra == letras[indice]:
            acertos += 1
            print("Número de letras certas já: %d" % (acertos))
            # Adicionar a palavra final as letrinhas
            dinamica[indice] = letras[indice]
            #remover os indices que já foram:
            delindex.append(indice)
            print(delindex) #armazena os índices que já foram
        else:
            dinamica[indice] = "_"
    # Após percorrer, teve-se a tentativa
    tent += 1
    print("Número de tentativas %d" % (tent))
    # Puxar método para imprimir a forquinha lá
    # game.print()

    print("Palavra até o momento %s" % (dinamica))

    if acertos == len(palavra) and tent < tentativas:
        status = True  # Adivinhou tudo
        print("Você ganhou o jogo")

    if tent >= tentativas:
        status = True  # Acabou
        print("Você perdeu")


