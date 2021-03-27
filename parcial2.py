print()
lista1=[]
lista2=[]
class admin_lista:

  contactos=[]

  def mostrar():
    nom=input("Intoduzca su nombre: ")
    lista1.append(f"Nombre: {nom}\n")
    telefono=int(input("Digite su numero telefonico: "))
    lista1.append(f"Telefono:{telefono}\n")
    gmail=input("Introduzca su gmail: ")
    lista1.append(f"gmail: {gmail}\n")
    direcc=input("Introduzca su direccion: ")
    lista1.append(f"Direccion: {direcc}\n")
    opcion=int(input("que opcion deseas: \n " 
    "1-Crear Contacto.\n"
    "2-Lista Telefono.\n"
    "3-Buscar contacto.\n"
    "4-Modificar su telefono,gmail o dirrecion.\n"
    "5-Salir.\n"
    "escriba la opcion aqui: "))

    if opcion==1:
      nombre1=input("Intoduzca su nombre:")
      lista2.append(f"Nombre2: {nombre1}\n")
      tel1=int(input("Digite su numero telefonico: "))
      lista2.append(f"Nuevo Telefono: {tel1}")
      email1=input("Introduzca su email: ")
      lista2.append(f"Nuevo Email {email1}\n")
      direccion1=input("Introduzca su direccion: ")
      lista2.append(f"Nueva Dirrecion: {direccion1}\n")
      print("continuacion......")

    elif opcion==2:
      print(f"La lista de su telefono es: \n{lista1}")
    elif opcion==3:
      buscar=input("introduzca el nombre del contacto: \n")
      if buscar==nom:
        print(lista1)
      elif buscar!=nom:
        print("Ese nombre no existe")
    elif opcion==4:
      tel2=int(input("escriba su numero telefonico:\n->"))
      lista1.append(f"Telefono: {tel2}\n")
      del lista1[1]
      gmail2=input("Introduzca su email:")
      lista1.append(f"Email: {gmail2}\n")
      del lista1[2]
      direcc2=input("Introduzca su direccion: ")
      lista1.append(f"Dirrecion: {direcc2}\n")
      del lista1[3]
      print("Has cambiado exitosamente.")
    elif opcion==5:
      print("gracias por visitar")
    else:
      print("Esa opcion no existe.")
  def lista():
    print(f"Contacto:\n{lista1}")

  mostrar()

admin_lista()
admin_lista.mostrar()
admin.lista()

