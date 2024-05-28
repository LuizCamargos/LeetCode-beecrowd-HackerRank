# -*- coding: utf-8 -*-

'''
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
'''
resultado=False
entrada = []
for i in range(4):
    entrada.append(int(input()))
if entrada[0]%2==0:
    if entrada[1]>entrada[2] and entrada[3]>entrada[0]:
        if entrada[2]+entrada[3]>entrada[0]+entrada[1]:
            if entrada[2]>=0 and entrada[3]>=0:
                resultado = True
string = "Valores aceitos" if resultado else "Valores nao aceitos" 
print(string)
