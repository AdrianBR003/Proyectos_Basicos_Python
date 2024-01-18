import random


chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()-_=+[]{}|;:".<>?/'
number = input('Introduce un numero entero del numero de contraseñas que necesite: ')
number = int(number)
length = input('Introduzca el tamaño de sus contraseñas: ')
length = int(length)

print('\n Aquí están sus contraseñas: ')

for pwd in range(number): 
    password = ''
    for c in range(length): 
        password += random.choice(chars)
    
    print(password)
    
    