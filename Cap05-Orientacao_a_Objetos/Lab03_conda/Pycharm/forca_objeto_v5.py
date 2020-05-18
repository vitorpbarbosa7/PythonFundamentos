board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:

    def __init__(self, palavra, status, tentativas, acertos, forca):
        self.palavra = palavra
        self.status = status
        self.tentativas = tentativas
        self.acertos = acertos
        self.maxtent = 7 #Já está intrínseco, não precisa atribuir lá em baixo (fixo)
        self.forca = forca

    #Método especial para o comprimento
    def __len__(self):
        return self.palavra

    def guess(self):
        self.letra = input("Digite uma letra \n")
        print("A letra digitada foi: %s" %(self.letra))
        return self.letra

    def print_desenho_forca(self):
        return word.forca

    def terminou(self):
        if word.tentativas >=word.maxtent:
            self.status = True
            print("Você perdeu")
            print("A palavra era: %s" % (self.palavra))
        return self.status

    def ganhou(self):
        if word.acertos == len(word.palavra):
            word.status = True  # Adivinhou tudo
            print("Você ganhou o jogo")

#Parte principal do código Main()
#Instanciando o objeto nome para pegar a palavra
word = Hangman("banana", False, 0,0,0)
getattr(word, "palavra")

# Inicializando indices e letras
indices = []
letras = []

for index, letra in enumerate(word.palavra):
    indices.append(index)
    letras.append(letra)

# Inicializando a lista vazia:
dinamica = ["_"] * len(letras)

# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
#print da forquinha

#Status inicial do jogo:
while word.status == False:
    #Instaciando o objeto\

    #letra = input("Digite uma letra \n")
    letra = word.guess() #solicita uma letra
    #print(letra) #Funcionou, guardou a letra a partir do método word.guess()
    teveacerto = False;
    # Percorrer os indices:
    for indice in indices:
        if letra == letras[indice]: #leitura do caracter
            word.acertos += 1
            teveacerto = True
            word.forca = word.forca
            print("Número de letras certas até o momento: %d" % (word.acertos))
            # Adicionar a palavra final as letrinhas
            if dinamica[indice] == "_":#Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = letras[indice]
            # remover os indices que já foram:
            elif dinamica[indice] == "_":#Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = "_"

    # Após percorrer, teve-se a tentativa
    word.tentativas += 1
    if teveacerto == False:
        word.forca += 1

    print("Palavra até o momento %s" % (dinamica))
    print("Até agora você errou %d vezes" %(word.forca))
    print(board[word.forca])
    print("Número de tentativas restantes %d" % (word.maxtent - word.tentativas))


    #Método para dizer que ganhou
    word.ganhou()

    #Chamando o método terminou para verificar se o jogo acabou ou não
    word.terminou()

# # Verifica o status do jogo
# game.print_game_status()
#
# print ('\nFoi bom jogar com você! Agora vá estudar!\n')
