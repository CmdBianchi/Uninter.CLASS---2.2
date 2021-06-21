##############################################################
#-----> EXERCISE 01

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o desconto: '))

desconto = preco * (p/100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
print('valor calculado de desconto: {}. valor final do produto {}'.format(desconto, final))
print('\n')
##############################################################
#-----> EXERCISE 02

km = int(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))

preco = 60 * dias + 0.15*km
print('Km = {}. Dias: {}.'.format(km, dias))
print('Valor a ser pago: {}'.format(preco))

##############################################################
#-----> EXERCISE 03

frase = input('Gite uma frase: ')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:])