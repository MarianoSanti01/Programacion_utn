import math
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
        while True:
            dni=input("ingrese su dni\n")
            condition=dni_verification(int(dni))
            if condition:
                break
        data=individual_token(name,surname,dni)
        if data != "":
            print(data)
#EJERCICIO 4
num1=int(input("ingrese el primer numero \n"))
num2=int(input("ingrese el segundo numero\n"))
if num2<num1:
    print("no hay multiplos entre esos numeros")
else:
    condition = multiple(num1,num2)
    if condition:
        print("los numeros ingresados son multiplos")
    else:
        print("los numeros ingresados no son multiplos")
#EJERCICIO 5(REVISAR)
from functions.numbers_addition import *
days=int(input("de cuantos dias quiere saber la temperatra media? \n"))
for i in range(days):
    print("dia ",i)
    max_temp=int(input("ingrese temperatura maxima del dia en celsius del dia \n"))
    minimal_temp=int(input("ingrese temperatura minima del dia en celcius del dia \n"))
    mid_temp=middle_temp(max_temp,minimal_temp)
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
shop_cart={
    "modulo":[12000,25],
    "pin":[500,5],
    "glass":[4000,30]
}
discounts=discount(shop_cart)
print("el precio final de los productos del carrito es",sum(discounts))
#ejercicio 11

numbers=[1,2]
multiplication=caller(called,numbers)
print("la multiplicacion de 1 * 2 es ",multiplication)
#ejercicio 12
phrase=input("ingrese su frase")
dictionary=create_dictionary(phrase)
print(dictionary)
#EJERCICIO 13
total=0
index=1
while True:
    print("ingrese el cuadrado",index, "o 0 para terminar de ingresar cuadrados")
    square=int(input())
    if(square != 0):
        total=sum_squares(square,total)
    else:
        break
    index+=1
print("el modulo es de: ",round(total**0.5,2))
#EJERCICIO 14 
num=input("ingrese que número desea saber si el primo\n")
condition=is_prime_number(int(num))
if condition or (int(num)==1) or (int(num)==0):
    print(num+" es un número primo")
else:
    print(num+" no es un numero primo")
#EJERCICIO 15
from functions.numbers_addition import *
total=1
while True:
    num=int(input("ingrese numero para saber su factorial o 0 para terminar\n"))
    if(num==0):
        break
    elif(num<0):
        print("numero no valido ingrese uno postivo")
    else:
        grafic_factorial=show_facorial(num,total)
        total=facorial(num,total)
    total=1
#EJERCICIO 16
while True:
    num=int(input("ingrese un numero\n"))
    digit=int(input("ingrese digito\n"))
    
    condition_num=number_verification(num)#verificacion para que se ingrese un numero
    condition_digit=number_verification(digit)#verificacion para que el digito ingresado sea numero
    condition_digit2=sigle_digit_verification(digit)#vefificacion para que solo se ingrese un digito
    
    if(condition_num and condition_digit and condition_digit2):
        digit_in_number=digit_times_in_number(num,digit)
        print("el digito ",digit," se encuentra ",digit_in_number," veces en el numero ",num)
        break
    else:
        print("datos invalidos ingreselos otra vez")
#EJERCICIO 17
from functions.numbers_addition import *
numbers=[]
while True:
    num=int(input("ingrese un numero primo o un numero no primo para terminar\n"))
    is_prime=is_prime_number(num)
    if not is_prime:
        print("FIN")
        break
    else:
        while True:
            digit=int(input("ingrese un digito\n"))
            digit_condition=sigle_digit_verification(digit)
            if not digit_condition:
                print("el digito debe ser solo un numero, vuelva a ingresarlo")
            else:
                counter=digit_times_in_number(num,digit)
                digits_sum=numbers_addition(num)
                print("el digito ingresado ",digit," se repite en el numero ",num,counter," veces")
                print("la suma de los digitos de ", num," es ",digits_sum)
                numbers.append(num)
                break
biggest=lowest_biggest(numbers)
total=1
biggest_factorial=facorial(biggest[0],total)
print("el mayor numero ingresado fue ",biggest[0]," y su factorial es ",biggest_factorial)