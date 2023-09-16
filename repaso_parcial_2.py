#EJERCICIO 1
phrase=input("ingrese una frase \n")
if(len(phrase)==4):
    print(phrase,"!")
else:
    print(phrase,"?")
#EJERCICIO 2
import random
my_list = ["hola","lol","python","xd","sssssooosl"]
chosen_world=random.choice(my_list)
chosen_world2=chosen_world
counter=0
guess=0
while True:
    if (counter==10 or guess==len(chosen_world2)):
        break
    else:
        print("intento ",counter+1," solo tinne 10 intenetos")
        letter = input("ingrese letra \n")
        if letter in chosen_world:
            for i in chosen_world:
                if i == letter:
                    index = chosen_world.find(letter)
                    chosen_world=chosen_world.replace(chosen_world[index],"",1)
                    guess += 1
            print("letra correcta")
        else:
            print("letra incorrecta")
        counter += 1
if(guess == len(chosen_world2)):
    print("GANASTE LA PALABRA ES: ",chosen_world2)
else:
    print("PERDISTE LA PALABRA ES: ",chosen_world2)
#EJERCICIO 3
phrase=input("ingrese texto \n")
phrase_li = phrase.split(" ")
print("en la oración ingresada hay ",len(phrase_li))
#EJERCICIO 4
month= input("asistio todo el mes? Y/N\n").lower()
hours= int(input("cuantas horas trabajo los domingos\n"))
if(month== "y"):
    if (hours<=5 and hours>=3):
        print("se adiciona el 3 porciento")
    elif (hours>=6 and hours < 11):
        print("se adiciona 10 porciento")
    else:
        print("no pudo trabajar esas horas. FIN")
elif (month=="n"):
    if(hours >=3 and hours<10):
        print("se adiciona el 2 porciento")
    else: print("no pudo trabajar esas horas. FIN")
else:
    print("caracter no valido y o n")
#EJERCICIO 5
num1=int(input("ingrese el primer numero \n"))
num2=int(input("ingrese el segundo numero\n"))
if (num1==num2):
    print("los numeros son iguales la multiplicacion de ",num1," x ",num2," = ",num2*num1)
elif(num1>num2):
    print("numero 1 es mayor la resta de ",num1," - ",num2," = ",num1-num2)
else:
    print("la suma de ",num1," + ",num2," = ",num2+num1)
#EJERCICIO 6
age = int(input("ingrese su edad\n"))
age_job= int(input("ingrese su antiguedad de empleo\n"))
if(age<60):
    if(age_job<25):
        print("no apto para cobrar ninguna jubilacion")
    else:
        print("abilitado para cobrar jubilacion por antiguedad joven")
else:
    if(age_job<25):
        print("abilitado para cobrar jubilacion por edad")
    elif(age_job>=25):
        print("abilitado para cobrar jubilacion por antiguedad adulta")
#EJERCICIO 7
age_job=int(input("¿cuantos años lleva en la empresa?\n"))
if(age_job<0):
    print("imposible. FIN")
else:
    if (age_job<1):
        print("su utilidad es del 5 por cientod del salario")
    elif(age_job==1):
        print("su utilidad es del 7 por ciento del salario")
    elif(age_job>=2 and age_job<5):
        print("su utilidad es del 10 porciento del salario")
    elif(age_job>=5 and age_job<10):
        print("su utilidad es del 15 por ciento del salario")
    elif(age_job>=10):
        print("su utilidad es del 20 por ciento del salario")