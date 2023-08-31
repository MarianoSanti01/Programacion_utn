import math
#ejercisio 1
word = input("ingrese la palabra ")
times = int(input("cunatas vesces se va a repetir la palabra "))
for i in range(times):
    print(i+1," - ",word)
#ejercisio 2
age = int(input("cual es su edad "))
for i in range(age):
    print("ha cumplido ",i+1," años")
#ejercisio 3
all_number=""
number=int(input("ingrese numero entero positivo "))
if number<=0:
    print("numero no valido")
for i in range(number):
    aux = str(i+1)
    all_number += aux + ", "
print(all_number)
#ejercisio 4
number=int(input("ingrese numero "))
if number<=0:
    print("numero no valido  ")
while number>0:
    print(number)
    number=number-1
#ejercisio 5
income=int(input("cantidad a invertir "))
investment_anual = int(input("cual es el interes anual? "))
years=int(input("ingrese cantidad de años "))
total=0
for i in range(years):
    total = total + investment_anual
    print("la inversion despues de ",i+1," años es de: ",income+total)
#ejercisio 6
long=int(input("de que largo sera el triangulo? "))
for i in range(long+1):
    triangle=""
    for j in range(i):
        triangle+="*"
    print(triangle)
#ejercisio 7
for i in range(10):
    for j in range(10):
        print(i+1," x ", j+1, " = ", (i+1)*(j+1))
#ejercisio 8

long=int(input("ingrese el numero entero? "))

if long<=0:
    print("numero no valido")
else:
    if(long % 2 == 0):
        for i in range(long+1):
            triangle=""
            if (i%2 == 0):
                aux=i
                while aux>0:
                    if(aux%2 == 0):
                        aux2=str(aux)
                        triangle += aux2
                    aux=aux-1
            print(triangle)
    else:
        for i in range(long+1):
            triangle=""
            if (i%2 != 0):
                aux3=i
                while aux3>0:
                    if(aux3%2 != 0):
                        aux4=str(aux3)
                        triangle += aux4
                    aux3=aux3-1
            print(triangle)
#preguntar por espacios vacios
#ejercisio 9
password="lol"
intento = input("ingrese su contraseña ")
while password != intento :
    intento = input("contraseña incorrecta. ingrese su cotraseña ")
#ejercisio 10
number=int(input("ingrese numero "))
counter=0
for i in range(number):
    if(number%(i+1)==0):
        counter=counter+1
if(counter==2):
    print("numero ingresado es primo")
else:
    print("numero ingresado no es primo")
#ejercisio 11
word=input("ingrese palabra ")
long=len(word)
for i in range(long):
    print(word[(long-1)-i])
#ejercisio 12
word = input("ingrese su palabra ")
letter = input("ingrese letra ")
counter=0
if(len(letter)>1):
    print("debe ingresar una sola letra ")
longi=len(word)
for i in range(longi):
    if(word[i] == letter):
        counter=counter+1
print("la letra ",letter," se repite ",counter," veces")
#ejercisio 13
word=input("ingrese palabra ").lower()
while word != "salir":
    for i in range(2):
        print(word)
    word=input("ingrese palabra ").lower()
#ejercisio 14
number=input("ingrese los numeros ")
n_splited=n.split(" ")
number1=int(n_splited[0])
number2=int(n_splited[1])
if(number2<number1):
    print("numero no validos, el primero debe ser menor")
else:
    for number1 in range(number2+1):
        if(number1% 2 == 0):
            print(number1," es par")
        else:
            print(number1," no es par")
#ejercisio 15
number=int(input("ingrese numero "))
for i in range(number+1):
    if(number%(i+1)==0):
        print(i+1," es divisor de ")
#ejercisio 16
number=int(input("cuantos numero se va a introducir "))
negatives=0 
if(number<0):
    print("numero invalido")
else:
    for i in range(number):
        print("escriba valor",i+1)
        value=int(input())
        if value < 0:
            negatives=negatives+1
    print("hay ",negatives," numeros negativos")
#ejercisios 17
vowels="aeiou"
phrase=input("ingrese frase ")
longi=len(phrase)
letters=""
for i in range(longi):
    if(phrase[i] in vowels):
        indice=vowels.find(phrase[i])
        letters += vowels[indice]
print("las vocales en la frase son: ",letters)
#ejercisio 18
n=10
a=0
b=1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c
#ejercision 19
number=int(input("cual es el objetivo de ahorro "))
savings = 0
while savings < number:
    savings=savings+int(input("ingrese monto a guardar "))

print("total ahorrado: ",savings)
#ejercisio 20
number=int(input("ingrese numero "))
total=0
all_number=""
while number !=0:
    all_number+=str(number)+" + "
    total=total+number
    number=int(input("ingrese numero "))
print("la suma de: ",all_number," es de: ",total)
#ejercisio 21
number=int(input("ingrese numero "))
highest_number=n
saved_number=""
while number!=0:
    saved_number+=str(number)+" + "
    number=int(input("ingrese numero "))
    if (number>highest_number):
        highest_number=number
print("el mayor numero ingresado entre ",saved_number, " fue ",highest_number)
#ejercisio 22
number=int(input("ingrese numero entero postivo"))
counter=0
while number != -1:
    aux=number
    dig=0
    dig2=""
    mini_total=0
    while aux>0:
        dig=aux%10
        dig2+=str(dig) + " + "
        mini_total=mini_total+dig
        if(number%2==0):
            counter=counter+1
        aux = math.floor(aux/10)
    print("la suma de ",dig2," es de ",mini_total)
    number=int(input("ingrese numero entero postivo"))
print(counter," numeros de los ingresados fueron pares")
#ejercisio 23 y 24
number=int(input("ingrese numero entero postivo "))
total=0
while number != 0:
    if(number<0):
        print("porfavor ingrese un monto positivo")
        number=int(input())
    else:
        number2=str(number)
        total=total+number
        number=int(input("ingrese numero entero postivo "))
if(total>1000):
    print("el monto es de: ",total,"se aplica 10 porciento descuento el total es de",total-(total*0.10) )
else:
    print("el total es de: ",total)
#ejercisio 25
number=int(input("ingrese numero entero postivo "))
all_numbers=""
total=0
if(number<0):
    print("numero no permitido")
elif(number==0):
    print("el factorial es de1")
else:
    for i in range(number):
        all_numbers += str(i)+" + "
        total=total+i
    print("la suma de ",all_numbers," = ",total)