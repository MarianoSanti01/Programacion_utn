from functions.numbers_addition import *
#EJERCICIO 1
dni= int(input("ingrese su dni\n"))
validation=dni_verification(dni)
if validation:
    print("dni valido")
else:
    print("dni no valido")
    
#EJERCICIO 2

phrase=input("ingrese la frase\n")
last_word=long_last_word(phrase)
print("la longitud de la ultima palbara es de: ",last_word)

#EJERCICIO 3
while True:
    name=input("ingrese su nombre \n")
    surname=input("ingrese su apellido\n")
    if (name == ""):
        print("FINAL")
        break
    else:
        dni=bucle_dni()
        data=individual_token(name,surname,dni)
        if data != "":
            print(data)
#EJERCICIO 4
num1=int(input("ingrese el primer numero \n"))
num2=int(input("ingrese el segundo numero\n"))
condition = multiple(num1,num2)
if condition:
    print("los numeros ingresados son multiplos")
else:
    print("los numeros ingresados no son multiplos")
#EJERCICIO 5(REVISAR)
days=int(input("de cuantos dias quiere saber la temperatra media? \n"))
for i in range(days):
    mid_temp=middle_temp(i+1)
    print("la temperatura minima del dia",i ,"es de: ",mid_temp)
#EJERCICIO 6
phrase=input("ingrese frase\n")
new_phase=phrase_with_spaces(phrase)
print(new_phase)
#EJERCICIO 7
numbers=input("ingrese los numeros separados por un espacio\n")
number_li=numbers.split(" ")
data=lowest_biggest(number_li)
print("el mayor numero ingresado es ",data[0]," y el menor es ",data[1])
#EJERCICIO 8
radio=int(input("ingrese el radio de la circunferencia\n"))
data=circuferance_data(radio)
print("el area de la circunferencia es de ",data[0]," y su perimetro es de ",data[1] )
#EJERCICIO 9
counter = 1
while True:
    username=input("ingrese su usuario\n")
    password=input("igrese su contraseña\n")
    if(counter < 3 or validation):
        validation=loggin(username,password)
        counter +=1
        if(validation):
            print("---bienvenido ",username," ---")
            break
    else:
        print("---limite de intentos alcansado, intentelo mas tarde---")
        break
#EJERCICIO 10
from functions.numbers_addition import *
shop_cart={
    "modulo":[12000,25],
    "pin":[500,5],
    "glass":[4000,30]
}
discounts=discount(shop_cart)
print("el precio final de los productos del carrito es",sum(discounts))
#ejercicio 11
