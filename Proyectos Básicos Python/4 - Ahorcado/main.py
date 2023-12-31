import random
from palabras import words
import string


def palabra_valida(words): 
    word = random.choice(words)  #Palabra aleatoria del diccionario 
    while '-' in word or ' ' in word: #Imponemos la condicion, donde decimos que mientras haya espacio o guion, que la omita
        word = random.choice(words)
    return word

"""
#ALGUNOS CONCEPTOS CLAVE: 

 >> 'set' es una coleccion desordenada de elementos únicos e inmutables 
   > Cuando usamos 'word_letters': Almacenamos letras unicas de la palabra a adivinar, y a medida que el usuario las va descubriendo, se van eliminando 
   > 'alphabet': Contiene todas las letras del alphabeto en mayúsculas para evitar errores al comparar, y la utilizamos para saber que el caracter introducido es valido 
   > 'used_letters': Guarda las letras que el usuario ha intentado adivinar.

>> 
"""


def juego():
    word = palabra_valida(words)
    word_letters = set(word.upper())
    used_letters = set()
    
    
    lives = 6
    
    while word_letters and lives > 0:
        print('Tienes', lives, 'vidas. Has usado las siguientes letras:', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Palabra actual:', ' '.join(word_list))

        user_letter = input('Ingresa una letra: ').upper()
        
        if user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.discard(user_letter)
                print('Letra acertada!') 
                # Actualizar word_list para mostrar la letra adivinada
                word_list = [letter if letter in used_letters else '-' for letter in word]
                print('Palabra actual:', ' '.join(word_list))
            else:   
                lives -= 1
                print('La letra no es correcta.')
        else:
            print('Ya has usado esta letra')

    if lives == 0: 
        print(f'Has perdido. La palabra era: {word}')
    else: 
        print('¡Felicidades, has ganado!')


juego()
