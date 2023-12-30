"""
Segundo proyecto de Python: Adivina el número del juego (usuario)
"""
import random


def computer_guess(x): 
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c': 
        guess = random.randint(low, high)
        feedback = input(f'Es {guess} más alto que (H), más bajo (L), o es correcto (C)??').lower()
        if feedback == 'h': 
            high = guess -1 
        elif feedback == 'l': 
            low = guess + 1
    print(f'El programa encontró el numero correcto {guess}')

    
computer_guess(10)
