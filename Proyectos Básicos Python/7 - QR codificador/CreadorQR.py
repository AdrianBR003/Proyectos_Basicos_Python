import qrcode 


data = 'Nunez mariquita de playa'

img = qrcode.make(data)

img.save('C:/Users/Usuario/Desktop/myqrcode.png')


