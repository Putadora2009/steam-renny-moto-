import os

ARCHIVO_DATOS = "usuarios.txt"

def registrar_usuarios(usuario, contrasena):
    if usuario == "" or contrasena == "":
        print("Error: los campos no pueden estar vacíos.")
        return False
    with open(ARCHIVO_DATOS, 'a', encoding="utf-8") as archivo:
        archivo.write(f"{usuario},{contrasena}\n")

    print(f"Exito: Usuario {usuario} registrado correctamente.")
    return True 

def iniciar_sesion(usuario, contrasena):
    # Corregida la indentación
    if not os.path.exists(ARCHIVO_DATOS):
        print("Error: los campos no pueden estar vacíos.")
        return False
    with open(ARCHIVO_DATOS, 'r', encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(',')

            if len(datos) == 2:
                user_guardado = datos[0]
                pass_guardada = datos[1]
            
                # Movido adentro para evitar errores si la línea del txt estaba vacía
                if user_guardado == usuario and pass_guardada == contrasena:
                    print(f"Bienvenido de nuevo, {usuario}!")
                    return True
                    
    # Añadido para que la interfaz sepa que falló el inicio de sesión
    return False