print("Bienvenido a CARGOMAX")
print("Registro de datos generales")

z = input("Registrar sus datos: ")

if (z == "SI") or (z == "si") or (z == "Si"):
    Nombres = input("Registar tus nombres: ")
    Apellidos = input("Registar tus apellidos: ")
    Genero = input("Registrar tu genero: ")
    DNI = input("Registrar tu DNI: ")
    print("Datos registrados con exito")
    print("Nombres: " + Nombres)
    print("Apellidos: " + Apellidos)
    print("Genero: " + Genero)
    print("DNI: " + DNI)
elif (z == "NO") or (z == "no") or (z == "No"):
     print("Tiene que registrarse")