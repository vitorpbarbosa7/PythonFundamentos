import random

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
========='''] #Declarando a variável assim, ela já fica como global
print(len(board))

class Hangman:

    def __init__(self, palavra, acertos, forca):
        self.palavra = palavra
        self.acertos = acertos
        self.forca = forca

    #Método especial para o comprimento
    def __len__(self):
        return self.palavra

    def guess(self):
        if word.forca < len(board) - 1 and word.acertos != len(word.palavra):
            self.letra = input("Digite uma letra \n")
            print("A letra digitada foi: %s \n" %(self.letra))
        return self.letra

    def print_desenho_forca(self):
        if word.forca < len(board)-1 and word.acertos != len(word.palavra):
            print(board[word.forca])
            print("A palavra até o momento é: %s \n" % (wordnow))
            print("Até agora você errou %d vezes \n:" % (word.forca))
            print("Número de tentativas restantes: %d \n" % (len(board)-1 - word.forca))

    def perdeu(self):
        if word.forca == len(board)-1:
            print(board[word.forca])
            print("Você perdeu")
            print("A palavra era: %s" % (self.palavra))

    def ganhou(self):
        if word.acertos == len(word.palavra):
            print("Palavra final: %s" %(word.palavra))
            print("Você ganhou o jogo")

def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        print(bank)
    return bank[random.randint(0, len(bank)-1)].strip('\n')

#Parte principal do código Main()
#Instanciando o objeto nome para pegar a palavra

word = Hangman(rand_word(),0,0)

#Para conseguir testar o funcionamento do programa
print("A palavra gerada foi: %s" %(word.palavra))

# Inicializando indices e letras
indices = []
letras = []

for index, letra in enumerate(word.palavra):
    indices.append(index)
    letras.append(letra)

# Inicializando a lista vazia:
dinamica = ["_ "] * len(letras)

# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
#print da forquinha

#Status inicial do jogo:
while word.forca < len(board)-1 and word.acertos != len(word.palavra): #Quando chegar no comprimento do board, é porque acabou
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
            jaforampositivas.append(letras[indice])
            letras.remove(letras[indice]) #Atualizando o
            #word.forca = word.forca
            #print("Número de letras certas até o momento: %d" % (word.acertos))
            # Adicionar a palavra final as letrinhas
            if dinamica[indice] == "_ ":#Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = letras[indice]
            # remover os indices que já foram:
            elif dinamica[indice] == "_":#Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = "_ "

    # Após percorrer, teve-se a tentativa
    if teveacerto == False:
        word.forca += 1 #Errando
        print("Número de erros: %d " %(word.forca)) #Para fins de checagem enquando programando

    #Puxar o método que faz impressão
    wordnow = ' '.join(dinamica) #Concatenar a lista de strings

    #Verificar se o jogador perdeu
    word.perdeu()

    #Printar o tabuleirinho
    word.print_desenho_forca()

    #Método para dizer que ganhou
    word.ganhou()

