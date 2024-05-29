# -*- coding: utf-8 -*-

'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
'''
entrada = input()
entrada = [int(e) for e in entrada.split(" ")]
listaOrdenada = entrada.copy()
listaOrdenada.sort()
for i in listaOrdenada: print(i)
print()
for j in entrada: print(j)
