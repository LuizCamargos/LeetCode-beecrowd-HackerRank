# -*- coding: utf-8 -*-

'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
'''
entrada = input()
a, b = [int(e) for e in entrada.split(" ")]
if a<b:
    horas=b-a
elif a>b:
    horas=(b+24)-a
else:
    horas=24
print(f"O JOGO DUROU {horas} HORA(S)")
