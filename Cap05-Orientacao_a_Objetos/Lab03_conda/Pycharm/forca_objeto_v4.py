class Hangman:

    def __init__(self, palavra, status, tentativas, acertos):
        self.palavra = palavra
        self.status = status
        self.tentativas = tentativas
        self.acertos = acertos
        self.maxtent = 7

    def guess(self):
        self.letra = input("Digite uma letra \n")
        print("A letra digitada foi: %s" %(self.letra))
        return self.letra

    def terminou(self):
        if word.tentativas >=word.maxtent and word.acertos < len(word):
            self.status = True
            print("Você perdeu")
            print("A palavra era %s:" % (self.palavra))
        return self.status

    def ganhou(self):
        if word.acertos == len(word.palavra) and word.tentativas < word.maxtent:
            word.status = True  # Adivinhou tudo
            print("Você ganhou o jogo")

#Parte principal do código Main()
#Instanciando o objeto nome para pegar a palavra
word = Hangman("banana", False, 0,0)
getattr(word, "palavra")

# Inicializando indices e letras
indices = []
letras = []

for index, letra in enumerate(word.palavra):
    indices.append(index)
    letras.append(letra)

# Inicializando a lista vazia:
dinamica = [None] * len(letras)

# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
#print da forquinha

#Status inicial do jogo:
while word.status == False:
    #Instaciando o objeto\

    #letra = input("Digite uma letra \n")
    letra = word.guess() #solicita uma letra
    #print(letra) #Funcionou, guardou a letra a partir do método word.guess()

    # Percorrer os indices:
    for indice in indices:
        if letra == letras[indice]: #leitura do caracter
            word.acertos += 1
            print("Número de letras certas até o momento: %d" % (word.acertos))
            # Adicionar a palavra final as letrinhas
            if dinamica[indice] == "_" or dinamica[indice] == None: #Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = letras[indice]
            # remover os indices que já foram:
        elif dinamica[indice] == "_" or dinamica[indice] == None:  #Pela negativa eliminar a adição quando já há uma letra
            dinamica[indice] = "_"
    # Após percorrer, teve-se a tentativa
    word.tentativas += 1
    print("Número de tentativas %d" % (word.tentativas))
    # Puxar método para imprimir a forquinha lá
    # game.print()

    print("Palavra até o momento %s" % (dinamica))

    #Método para dizer que ganhou
    word.ganhou()

    #Chamando o método terminou para verificar se o jogo acabou ou não
    word.terminou()


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
