# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print('Selecione a operação desejada \n \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão')

operacao = int(input('Digite sua opção (1/2/3/4):'))
print(operacao)

def numeros():
	prinum = float(input("Digite o primeiro número: "))
	segnum = float(input("Digite o segundo número: "))
	return prinum, segnum 

if operacao == 1:
	(prinum, segnum) = numeros()
	soma = prinum + segnum
	print("O resultado da operação é %f" %(soma))
elif operacao == 2:
	(prinum, segnum) = numeros()	
	sub = prinum - segnum
	print("O resultado da operação é %f" %(sub))
elif operacao == 3:
	(prinum, segnum) = numeros()
	multi = prinum * segnum
	print("O resultado da operação é %f" %(multi))
elif operacao == 4:
	(prinum, segnum) = numeros()
	div = prinum / segnum
	print("O resultado da operação é %f" %(div))
else: 
	print("Você escolheu uma opção fora do intervalo de 1 a 4 ")



