import hashlib

# 3.- A partir de un contexto donde queremos almacenar un usuario y su contraseña, haz un ejemplo que explique cómo se haría:

# Función para cifrar contraseña
def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()
    return HashedPassword

# Usando una lista.

def menuUsuarioLista(usuarios):
    print("1- Crear un usuario\n2- Iniciar sesión\n3- Salir")
    menuInput = input('Elige una opción : ')
    match menuInput:
        case "1":
            crearUsuarioLista(usuarios)
        case "2":
            consultarUsuarioLista(usuarios)
        case "3":
            print("Adios")
        case _:
            print("Number not between 1 and 3")
            menuUsuarioLista(usuarios)


def crearUsuarioLista(usuarios):
    listaUsuarios = usuarios
    # for i in range(5):
    usuario = input('Nombre de usuario: ')
    contraseña = input('Contraseña: ')
    contraseñaConHash = Sha512Hash(contraseña)
    nuevoUsuario = [usuario, contraseñaConHash]
    listaUsuarios.append(nuevoUsuario)
    menuUsuarioLista(usuarios)


def consultarUsuarioLista(usuarios):
    print(f"Usuarios: {usuarios[0][1]}")
    nombreUsuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")
    contraseña = Sha512Hash(contraseña)

    for i in range(len(usuarios)):
        if nombreUsuario == usuarios[i][0] and contraseña == usuarios[i][1]:
            print("Acceso concedido")
        else:
            print("Credenciales de inicio de sesión incorrectas, inténtelo de nuevo.")
            consultarUsuarioLista(usuarios)
    menuUsuarioLista(usuarios)

usuariosLista = []
menuUsuarioLista(usuariosLista)
print(usuariosLista)

# Usando una diccionario.
def crearUsuarioDiccionario(usuarios):
    listaUsuarios = usuarios
    # usuarios = [["Pepe","1234"],["Juan","5678"],["Carmen","9101112"],["Sara","131415"],["Jose","161718"]]

    # print("1- Crear un usuario\n2- Consultar un usuario\n3- Salir")
    for i in range(5):
        usuario = input('Nombre de usuario: ')
        contraseña = input('Contraseña: ')
        contraseñaConHash = Sha512Hash(contraseña)
        usuarios[usuario] = contraseñaConHash
    print(listaUsuarios)


def consultarUsuarioDiccionario(usuarios):
    print(usuarios)
    for i in range(2):
        usuario = input('¿Qué usuario quieres consultar? ')
        if usuario in usuarios == True:
            print("Si existe")
        else:
            print("No existe")
usuariosDiccionario = {}
#crearUsuarioDiccionario(usuariosDiccionario)
