# -*- coding: utf-8 -*-

'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
'''
entrada = float(input())+0.001 #0.0001 serve para corrigir erro de execução causado pelo arredondamento do float
notas = [100,50,20,10,5,2]
moedas = [1, .5, .25,.1,.05, .01]

print("NOTAS:")
for nota in notas:
    n, entrada = divmod(entrada, nota)
    print(f"{int(n)} nota(s) de R$ {nota:.2f}")


print("MOEDAS:")
for moeda in moedas:
    n, entrada = divmod(entrada, moeda)
    print(f"{int(n)} moeda(s) de R$ {moeda:.2f}")
