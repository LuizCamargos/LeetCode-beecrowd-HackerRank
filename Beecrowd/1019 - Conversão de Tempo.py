# -*- coding: utf-8 -*-

'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
'''

seconds = int(input())
horas = seconds//3600
seconds%=3600
minutos = seconds//60
seconds%=60

print(f"{horas}:{minutos}:{seconds}")
