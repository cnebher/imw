def show_contacts(phone_book):
    if phone_book == {}:
        print("¡No hay contactos en la agenda!")
    else:
        for name, phone_number in phone_book.items():
            print(name, ":", phone_number)
def add_contact(phone_book, name, phone_number):

        phone_book[name] = phone_number
def remove_contact(phone_book, name):

    if name in phone_book:
        del(phone_book[name])
    else:
        print("El contacto no existe")
def menu():
    phone_book = {}

    while True:
        print("\n1-Lista de contactos")
        print("2-Añadir contacto")
        print("3-Borrar contacto")
        print("4-Salir\n")

        menu = input("¿Qué opción deseas elegir?: ")

        if menu == "1":
            show_contacts(phone_book)
        elif menu == "2":
            name = input("Contacto que deseas añadir: ")
            if name not in phone_book:
                phone_number = input("¿Qué número tiene el contacto?: ")
                add_contact(phone_book, name, phone_number)
            else:
                print("El contacto introducido ya existe")
        elif menu == "3":
            name = input("Elimina el contacto: ")
            remove_contact(phone_book, name)
        elif menu == "4":
            break
        else:
            print("Opcion incorrecta!")

menu()
