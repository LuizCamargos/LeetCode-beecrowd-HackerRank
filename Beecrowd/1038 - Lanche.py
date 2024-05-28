# -*- coding: utf-8 -*-

'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar
'''
valores = [4,4.5,5,2,1.5]
cod, qtd = input().split(" ")
total = valores[int(cod)-1]*int(qtd)
print(f"Total: R$ {total:.2f}")
