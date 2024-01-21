from pyzbar.pyzbar import decode 
from PIL import Image


img = Image.open('C:/Users/Usuario/Desktop/myqrcode.png') #Directorio
result = decode(img)

print(result)