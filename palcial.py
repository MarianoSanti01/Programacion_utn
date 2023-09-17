'''
Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
Generar un menú de opciones, que serán:
Juego de números.
Juego de palabras.
Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando 
ingrese 0). Al finalizar mostrar por pantalla:
El mayor número par.
El promedio de los números impares.
Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y
 mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
No olvides realizar las debidas validaciones!
'''
name=input("ingrese su nombre\n")
counter =0

operation = input("hola "+name+" ingrese 1 para juego de numero o 2 para juego de letras\n")
if (operation=="1"):
    total_odd=0
    counter_odd=0
    biggest=0
    while True:
        number=int(input(name+" ingrese numero entero o 0 para salir del juego por favor\n"))
        if(number==0):
            break
        else:      
            if(number % 2 == 0):
                if(counter==0):
                    biggest=number
                else:
                    if number>biggest:
                        biggest=number
            else:
                total_odd += number
                counter_odd += 1
        counter += 1
    if(total_odd>0 and counter_odd>0):
        print(name," el mayor numero par ingresado es: ",biggest," y el promedio de los numeros impares es: ",(total_odd/counter_odd))
    else:
        print(name," el mayor numero par ingresado es: ",biggest)
elif (operation=="2"):
    counter_vowels =0
    word=input(name+" ingrese palabra\n").lower()
    for i in word:
        if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            counter_vowels +=1
    print("la palabra ingresada contiene ",counter_vowels," vocales\n")
else:
    print(name+" esa operacion no es valida 1,2 o 0 porfavor")
