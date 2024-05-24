# -*- coding: utf-8 -*-

'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''
id = int(input())
hr_trabalhada = int(input())
salario_hora = float(input())


print(f"NUMBER = {id}")
print(f"SALARY = U$ {salario_hora*hr_trabalhada:.2f}")
