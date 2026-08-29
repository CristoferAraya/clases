opcion = 0
usuario = ""
password = ""
while (opcion !=3):
    print("=====Menu de usuarios=====")
    print("1.- Registrar usuario")
    print("2.- Mostrar usuario ")
    print("3.- Iniciar sesion")
    print("4.- Salir")

    opcion = int(input("Ingresa la opcion : "))

    match (opcion):
        case 1:
            usuario = input("Ingresa el usuario :")
            password = input("Ingresa la password :")

        case 2:

            if usuario =="":
                print("Aun no ingresas ningun usuario")
            else:
                print(f"El usuario ingresado es  {usuario}")
        case 3:
            while True:
                password_ingresada = input("Ingresa la password : ")
                if (password == password_ingresada):
                    print("logeado")
                    break
                else:
                    print("password incorrecta")

        case 4:
            print("Muchas gracias, adios\n")
        case _:
            print("Opcion invalida \n")