# -*- coding: utf-8 -*-

'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
'''
nota=[]
for i in range(0,3):
    nota.append(float(input())+0.01) #corrige precisão do float
media = nota[0]*2+nota[1]*3+nota[2]*5
media = media/10

print(f"MEDIA = {media:.1f}")
