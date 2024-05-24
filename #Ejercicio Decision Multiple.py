#Ejercicio Decision Multiple

print("-----BIENVENIDO A BURGER KING-----")
print("Ingrese los datos para su factura electrónica \n")
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cédula: ")
correo = input("Ingrese su correo electrónico: ")
cantidad = int(input("Ingrese el número de hamburguesas a adquirir: "))
print()
print("Por favor, seleccione el tipo de hamburguesa a adquirir:")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
numero = int(input("Ingrese el número: ")) 
if numero == 1 or numero == 2 or numero == 3:
    if numero == 1:
        precio = cantidad * 1.50
    elif numero == 2:
        precio = cantidad * 2.50
    elif numero == 3:
        precio = cantidad * 3.25
    print()
    print("Ingrese su método de pago: ")
    print("1) Tarjeta de crédito o 2) Efectivo")
    numero2 = int(input("Ingrese la opción de su preferencia: "))
    print()
    if numero2 == 1:
        print(f"Genial, {nombre} el precio final es de: ${precio + (precio*0.05):.2f}") 
        print(f"Tu factura será enviada a: {correo}")  
    elif numero2 ==2:
        print(f"Genial, {nombre} el precio final es de: ${precio:.2f}") 
        print(f"Tu factura será enviada a: {correo}")  
    else:
        print("-----------------------------------------")
        print("No existe ese tipo de pago:")
        print("Muchas gracias")
        print("-----------------------------------------")
else:
    print("-----------------------------------------")
    print("Ese tipo de hamburguesa no existe")
    print("Muchas gracias")
    print("-----------------------------------------")