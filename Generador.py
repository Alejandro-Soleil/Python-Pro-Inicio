import random
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
longitud = int(input("Ingrese la longitud de la contraseña: "))
contrasena = ""

for i in range(longitud):
    contrasena += random.choice(caracteres)
print("La contraseña generada es:", contrasena)
