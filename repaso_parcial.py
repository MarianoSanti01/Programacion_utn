#BLock de notas
#modificación 1 de cuando se mostro en clase, ahora la opcion 2 no borra todo lo escrito, pide cuantas palabras se borraran y elemina ese numero
#modificación 2 se elimino la opcion de mostrar lo escrito para mostrarlo simpre despues de realizar alguna operacion.
content = ""
aux =""
while True:
    print("\n menu de operaciones: \n 1.añadir texto \n 2.borrar texto \n 3.buscar cuantas veces se imprimio una palabra \n 4.salir del programa \n ")
    operation=input()
    if(operation == "1"):
        print("texto a ingresar: \n")
        new_text=input()
        content = content+" "+new_text
        content_arr = content.split(" ")
    elif (operation == "2"):
        if (content == ""):
            print("no hay nada que revertir")
        else:
            deleate=int(input("cuantas palabras borrara?"))
            index=len(content_arr)-deleate
            if(index<0):
                print("no se pueden borrar tantas palabras")
            else:
                while len(content_arr)>index:
                    content_arr.pop()
                
    elif (operation == "3"):
        print("¿que palabra desea buscar?")
        word=input().lower()
        counter =0
        i=0
        for i in range(len(content_arr)):
            if(content_arr[i].lower()==word):
                counter += 1
        print("la palabra ",word, "se muestra un total de: ", counter," veces")
    elif(operation == "4"):
        break
    else:
        print("operacion invalida")
    content=""
    for i in content_arr:
        content += " "+i
    print(content)