print("*********-Bienvenido-*******")
nombreCliente=input("Ingrese su nombre: ")
numeroCedula=int(input("Ingrese su numero de cedula: "))
correo=input("Ingrese su correo: ")
numHamburguesas=int(input("Ingrese el numero de hamburguesas: "))
print ("Ingrese el tipo de hamburguesa")
tipoHamburguesa=int(input("1) simple 2) doble 3) triple  "))
if tipoHamburguesa == 1 or tipoHamburguesa==2 or tipoHamburguesa==3:
    if tipoHamburguesa==1 :
        precio = numHamburguesas*1.50
    elif tipoHamburguesa==2:
        precio = numHamburguesas*2.50
    elif tipoHamburguesa==3:
        precio = numHamburguesas*3.25
    print("Ingrese la forma de pago")
    tipoPago = int (input("1) Tarjeta 2) Efectivo  "))
    if tipoPago == 1:
        recargo = precio *0.05
        pf = precio + recargo
        print("El precio final es de $" ,pf)
    elif tipoPago == 2:
        print("El precio final es de $", precio)
    else:
        print("No existe ese tipo de pago")
        print("Muchas gracias")
else :
    print("Ese tipo de hamburguesa no existe")
    print("Muchas gracias")
        
        
        
        