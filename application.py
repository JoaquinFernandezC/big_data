import mongo_connection

def ask_option_menu():
    print(' 1. Revisar historial de tono promedio\n'
          ' 2. Revisar...')
    opt = int(input('Ingrese opción: '))
    return opt


if __name__=="__main__":
    option = ask_option_menu()
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    events = mongo_connection.get_events_collection()
    for event in events.find({}):
        print (event)
        break