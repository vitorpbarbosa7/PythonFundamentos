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
            print("Número de acertos até o momento: %d \n" %(word.acertos))
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

#Selecionar aleatoriamente uma palavra do banco de dados
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        print(bank)
    return bank[random.randint(0, len(bank)-1)].strip('\n')

#Parte principal do código Main()
#Instanciando o objeto nome para pegar a palavra

#Main começa aqui
word = Hangman(rand_word(),0,0)

#Para conseguir testar o funcionamento do programa
print("A palavra gerada foi: %s" %(word.palavra))

# Inicializando indices e letras
indices = []
letras_original = []

for index, letra in enumerate(word.palavra):
    indices.append(index)
    letras_original.append(letra)

letras = letras_original #A original é letras_
print(letras)
jaforamcertas = []
jaforamerradas = []
jaforamtodas = []

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

    if letra in jaforamcertas and teveacerto == False:
        print("Você já digitou a letra certa %s" %(letra))

    #Varrer uma vez a palavra, ao digitar uma letra
    for indice in indices:
        teveacerto = False
        if letra == letras[indice] and letra not in jaforamcertas: #leitura do caracter
            word.acertos += 1
            teveacerto = True
            print("entrou")
            jaforamcertas.append(letras[indice])  # Guardar as que já chutaram))
            # Adicionar a palavra final as letrinhas
            if dinamica[indice] == "_ ":#Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = letras_original[indice]
            # remover os indices que já foram:
            elif dinamica[indice] == "_":#Pela negativa eliminar a adição quando já há uma letra
                dinamica[indice] = "_ "

    print("As letras que já foram são estas:")
    print(jaforamcertas)


    # Após percorrer, teve-se a tentativa
    if teveacerto == False and letra not in jaforamcertas:
        word.forca += 1 #Errando
        jaforamerradas.append(letras[indice])
        print("Número de erros: %d " %(word.forca)) #Para fins de checagem enquando programando

    #Isto aqui ainda está dentro do while!!

    #Puxar o método que faz impressão
    wordnow = ' '.join(dinamica) #Concatenar a lista de strings

    #Verificar se o jogador perdeu
    word.perdeu()

    #Printar o tabuleirinho
    word.print_desenho_forca()

    #Método para dizer que ganhou
    word.ganhou()
##Tudo isso dentro do While (Main do lab03)
#------------------------------------------------------------------------------------#
