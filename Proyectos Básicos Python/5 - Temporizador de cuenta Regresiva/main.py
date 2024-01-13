""" NOTAS: 
    *Desactivar Extension Error Lens
    1.- Le preguntaremos al usuario la cantidad de numeros que contar 
    regresivamente
    2.- divmod devuelve un par de valores, el cociente y 
    el resto de la division
    divmod(x, y) devuelve un par de valores, el cociente 
    de la división entera de x por y el resto de esa división 
    En este caso, mins, secs = divmod(t, 60) da 
    como resultado la cantidad de minutos completos y el resto da como 
    resultado la cantidad de segundos restantes
"""


import time 


def countdown(t):
    while t: 
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Coloca mins y sec en ese formato
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
    print('Tiempo completado!')
    
    
t = input('Introduce el tiempo en segundos')
countdown(int(t))

