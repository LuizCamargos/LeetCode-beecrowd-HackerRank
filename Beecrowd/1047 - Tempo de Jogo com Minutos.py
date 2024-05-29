# -*- coding: utf-8 -*-

'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
'''
entrada = input()
lista = [int(e) for e in entrada.split(" ")]

a = lista[0]*60+lista[1]
b = lista[2]*60+lista[3]
if a<b:
    minutos=b-a
elif a>b:
    minutos=(b+1440)-a
else:
    minutos=1440
print(f"O JOGO DUROU {minutos//60} HORA(S) E {minutos%60} MINUTO(S)")
