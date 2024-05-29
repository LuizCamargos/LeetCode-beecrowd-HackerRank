# -*- coding: utf-8 -*-

'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
Se o ponto estiver na origem, escreva a mensagem “Origem”.
Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.
'''
entrada = input()
x, y = [float(e) for e in entrada.split(" ")]

if x==0 and y==0:
    resultado = "Origem"
elif x!=0 and y==0:
    resultado = "Eixo X"
elif x==0 and y!=0:
    resultado = "Eixo Y"
else:
    if x>0.0:
        resultado = ("Q1" if y>0.0 else "Q4")
    elif x<0.0:
        resultado = ("Q2" if y>0.0 else "Q3")
print(resultado)
