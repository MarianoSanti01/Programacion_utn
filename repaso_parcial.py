#BLock de notas
content = ""
while True:
    print("\n menu de operaciones: \n 1.añadir texto \n 2.borrar documento \n 3.buscar cuantas veces se imprimio una palabra \n 4.leer lo ingresado \n 5.salir del programa")
    operation=input()
    if(operation == "1"):
        print("texto a ingresar: \n")
        new_text=input()
        content += ' / '+new_text
    elif (operation == "2"):
        if (content == ""):
            print("no hay nada que revertir")
        else:			
            content = ""
    elif (operation == "3"):
        print("¿que palabra desea buscar?")
        word=input().lower()
        counter =0
        value=0
        ar_content=content.split(" ")
        for world in ar_content:
            if(ar_content[value].lower()==word):
                counter += 1
                value +=1
            else:
                value +=1
        print("la palabra ",word, "se muestra un total de: ", counter," veces")
    elif(operation == "4"):
        print(content)
    elif(operation == "5"):
        break
    else:
        print("operacion invalida")