class Hangman:

    def __init__(self, palavra):
        self.palavra = palavra

    def guess(self):
        self.letra = input("Digite uma letra \n")
        print("A letra digitada foi: %s" %(self.letra))
        return self.letra

    def

status = False
# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
#print da forquinha
while status == False:
    #Instaciando o objeto\
    word = Hangman("banana")
    getattr(word, "palavra")

    #letra = input("Digite uma letra \n")
    word.guess() #solicita uma letra

    # Percorrer os indices:
    for indice in indices:
        if letra == letras[indice]: #leitura do caracter
            acertos += 1
            print("Número de letras certas já: %d" % (acertos))
            # Adicionar a palavra final as letrinhas
            if dinamica[indice] == "_" or dinamica[indice] == None: #Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = letras[indice]
            # remover os indices que já foram:
        elif dinamica[indice] == "_" or dinamica[indice] == None:  #Pela negativa eliminar a adição quando já há uma letra
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
        print("A palavra era %s:" %(palavra))

# # Verifica o status do jogo
# game.print_game_status()
#
# # De acordo com o status, imprime mensagem na tela para o usuário
# if game.hangman_won():
#     print ('\nParabéns! Você venceu!!')
# else:
#     print ('\nGame over! Você perdeu.')
#     print ('A palavra era ' + game.word)
#
# print ('\nFoi bom jogar com você! Agora vá estudar!\n')
