'''
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.
('Manuel Juarez', 12345678, 'San Juan')
'''
from functions.funciones_dimensionales import *
from functions.numbers_addition import dni_verification
pasangers=[]
destinys=[]
while True:
    aux=[]
    print("[0 salir del programa]-[1 agregar pasajeros]-[2 agregar destino][3 ver ciudad usando el dni]")
    print("[4 ver cantidad de pasajeros ingresando una ciudad]-[5 ver pais dado un DNI][6 dado un pais mostrar cuantos pasajeros viajan]")
    choise=input()
    if(choise=="0"):
        break
    elif(choise=="1"):
        name=input("agrege el nombre del pasajero\n").lower()
        while True:
            dni=int(input("agrege el DNI del pasajero\n"))
            validation=dni_verification(int(dni))
            if(validation):
                destiny=input("ingrese destino de pasajero\n").lower()
                aux.append(destiny)
                validation1=find_tuple_in_list(destinys,aux)
                if(not validation1):
                    country=input("la ciudad ingresada no esta registrada ¿de que pais es?\n").lower()
                    data=add_two_elements_in_tupla(destiny,country)
                    destinys.append(data)
                    new_pasager=add_three_elements_in_tupla(name,dni,destiny)
                    pasangers.append(new_pasager)
                    break
                else:
                    new_pasager=add_three_elements_in_tupla(name,dni,destiny)
                    pasangers.append(new_pasager)
                    break
            else:
                print("dni invalido vuelva a ingresarlo")
    elif(choise=="2"):#verificar si ciudad existe
        new_city=input("ingrese la ciudad\n").lower()
        new_country=input("ingrese pais de la ciudad\n").lower()
        data=add_two_elements_in_tupla(new_city,new_country)
        destinys.append(data)
    elif(choise=="3"):
        dni=int(input("ingrese el dni del pasajero\n"))
        aux.append(dni)
        data=find_tuple_in_list(pasangers,aux)
        if data:
            city=give_element_in_tupla(pasangers,aux,2)
            print("La ciudad encontrada con el dni ingresado es ",city[0])
        else:
            print("no se encontro pasajero con ese dni")
    elif(choise=="4"):
        city=input("ingrese la ciudad para ver sus pasajeros\n").lower()
        aux.append(city)
        counter=count_in_list_tuple(pasangers,aux)
        print(counter," personas viajaran a ",aux[0])
    elif(choise=="5"):
        dni=int(input("ingrese el dni del pasajero\n"))
        aux.append(dni)
        validation2=find_tuple_in_list(pasangers,aux)
        if validation2:
            city=give_element_in_tupla(pasangers,aux,2)
            aux.clear()
            aux.append(city)
            validation3=find_tuple_in_list(destinys,aux)
            if validation3:
                country=give_element_in_tupla(destinys,aux,1)
                print("el pasajero viajara a ",country[0])
            else:
                print("no se encontro la ciudad ingresada")
        else:
            print("no se encontro el dni ingresado")
    elif(choise=="6"):
        country=input("ingrese el pais para saber cuantos pasajeros viajaran\n")
        aux.append(country)
        validation4=find_tuple_in_list(destinys,aux)
        if validation4:
            city=give_element_in_tupla(destinys,aux,0)
            counter=count_in_list_tuple(pasangers,aux)
            print(counter," personas viajaran a ",country)
print(pasangers)
print(destinys)