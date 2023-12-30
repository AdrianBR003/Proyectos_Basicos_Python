"""
Tercer proyecto de Python: Piedra, papel o tijera
"""

import random; 


Lopciones = ['piedra', 'papel', 'tijera']
eleU = input('Introduzca "piedra", "papel" o "tijera" ').lower()
eleC = random.choice(Lopciones)


def ganador(eleU, eleC): 
    if (eleU == eleC): 
        print('Empate, siguiente ronda!')
        
    elif (eleU == 'piedra' and eleC == 'tijera') or (eleU == 'papel' and eleC == 'piedra') \
        or (eleU == 'tijera' and eleC == 'papel'): 
        print(f'Has ganado!!, el ordenador introdució {eleC}')
    else: 
        print(f'Has perdido!, el ordenador introducio {eleC}')


ganador(eleU, eleC)

