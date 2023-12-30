""" 
Primer proyecto de Python: Adivina el número del juego (computadora)
"""
import random


def guess(x): 
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Dame un numero entre 1 y {x}: '))
        if guess < random_number:     
            print('El numero que buscas es mayor al que has introducido')
        elif guess > random_number: 
            print('El numero que buscas es menor al que has introducido')
    print(f'Enhorabuena, has encontrado el numero {random_number}')


guess(10)
