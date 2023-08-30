import math
#ejercisio 1
palabra = input("ingrese la palabra ")
veces = int(input("cunatas vesces se va a repetir la palabra "))
for i in range(veces):
    print(i+1," - ",palabra)
#ejercisio 2
edad = int(input("cual es su edad "))
for i in range(edad):
    print("ha cumplido ",i+1," años")
#ejercisio 3
n_completo=""
n=int(input("ingrese numero entero positivo "))
if n<=0:
    print("numero no valido")
for i in range(n):
    auxiliar = str(i+1)
    n_completo += auxiliar + ", "
print(n_completo)
#ejercisio 4
n=int(input("ingrese numero "))
if n<=0:
    print("numero no valido  ")
while n>0:
    print(n)
    n=n-1
#ejercisio 5
inversion=int(input("cantidad a invertir "))
interes_anual = int(input("cual es el interes anual? "))
anos=int(input("ingrese cantidad de años "))
total=0
for i in range(anos):
    total = total + interes_anual
    print("la inversion despues de ",i+1," años es de: ",inversion+total)
#ejercisio 6
long=int(input("de que largo sera el triangulo? "))
for i in range(long+1):
    triangulo=""
    for j in range(i):
        triangulo+="*"
    print(triangulo)
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
            triangulo=""
            if (i%2 == 0):
                auxiliar=i
                while auxiliar>0:
                    if(auxiliar%2 == 0):
                        auxiliar2=str(auxiliar)
                        triangulo += auxiliar2
                    auxiliar=auxiliar-1
            print(triangulo)
    else:
        for i in range(long+1):
            triangulo=""
            if (i%2 != 0):
                auxiliar3=i
                while auxiliar3>0:
                    if(auxiliar3%2 != 0):
                        auxiliar4=str(auxiliar3)
                        triangulo += auxiliar4
                    auxiliar3=auxiliar3-1
            print(triangulo)
#preguntar por espacios vacios
#ejercisio 9
contraseña="lol"
intento = input("ingrese su contraseña ")
while contraseña != intento :
    intento = input("contraseña incorrecta. ingrese su contraseña ")
#ejercisio 10
n=int(input("ingrese numero "))
contador=0
for i in range(n):
    if(n%(i+1)==0):
        contador=contador+1
if(contador==2):
    print("numero ingresado es primo")
else:
    print("numero ingresado no es primo")
#ejercisio 11
palabra=input("ingrese palabra ")
long=len(palabra)
for i in range(long):
    print(palabra[(long-1)-i])
#ejercisio 12
palabra = input("ingrese su palabra ")
letra = input("ingrese letra ")
contador=0
if(len(letra)>1):
    print("debe ingresar una sola letra ")
longi=len(palabra)
for i in range(longi):
    if(palabra[i] == letra):
        contador=contador+1
print("la letra ",letra," se repite ",contador," veces")
#ejercisio 13
palabra=input("ingrese palabra ").lower()
while palabra != "salir":
    for i in range(2):
        print(palabra)
    palabra=input("ingrese palabra ").lower()
#ejercisio 14
n=input("ingrese los numeros ")
n_separados=n.split(" ")
n1=int(n_separados[0])
n2=int(n_separados[1])
if(n2<n1):
    print("numero no validos, el primero debe ser menor")
else:
    for n1 in range(n2+1):
        if(n1% 2 == 0):
            print(n1," es par")
        else:
            print(n1," no es par")
#ejercisio 15
n=int(input("ingrese numero "))
for i in range(n+1):
    if(n%(i+1)==0):
        print(i+1," es divisor de ")
#ejercisio 16
n=int(input("cuantos numero se va a introducir "))
negativos=0
if(n<0):
    print("numero invalido")
else:
    for i in range(n):
        print("escriba valor",i+1)
        valor=int(input())
        if valor < 0:
            negativos=negativos+1
    print("hay ",negativos," numeros negativos")
#ejercisios 17
vocales="aeiou"
frase=input("ingrese frase ")
longi=len(frase)
letras=""
for i in range(longi):
    if(frase[i] in vocales):
        indice=vocales.find(frase[i])
        letras += vocales[indice]
print("las vocales en la frase son: ",letras)
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
n=int(input("cual es el objetivo de ahorro "))
ahorros = 0
while ahorros < n:
    ahorros=ahorros+int(input("ingrese monto a guardar "))

print("total ahorrado: ",ahorros)
#ejercisio 20
n=int(input("ingrese numero "))
total=0
n_guadados=""
while n !=0:
    n_guadados+=str(n)+" + "
    total=total+n
    n=int(input("ingrese numero "))
print("la suma de: ",n_guadados," es de: ",total)
#ejercisio 21
n=int(input("ingrese numero "))
n_mayor=n
n_guadados=""
while n!=0:
    n_guadados+=str(n)+" + "
    n=int(input("ingrese numero "))
    if (n>n_mayor):
        n_mayor=n
print("el mayor numero ingresado entre ",n_guadados, " fue ",n_mayor)
#ejercisio 22
n=int(input("ingrese numero entero postivo"))
contador=0
while n != -1:
    auxiliar=n
    dig=0
    dig2=""
    mini_total=0
    while auxiliar>0:
        dig=auxiliar%10
        dig2+=str(dig) + " + "
        mini_total=mini_total+dig
        if(n%2==0):
            contador=contador+1
        auxiliar = math.floor(auxiliar/10)
    print("la suma de ",dig2," es de ",mini_total)
    n=int(input("ingrese numero entero postivo"))
print(contador," numeros de los ingresados fueron pares")
#ejercisio 23 y 24
n=int(input("ingrese numero entero postivo "))
total=0
while n != 0:
    if(n<0):
        print("porfavor ingrese un monto positivo")
        n=int(input())
    else:
        n2=str(n)
        total=total+n
        n=int(input("ingrese numero entero postivo "))
if(total>1000):
    print("el monto es de: ",total,"se aplica 10 porciento descuento el total es de",total-(total*0.10) )
else:
    print("el total es de: ",total)
#ejercisio 25
n=int(input("ingrese numero entero postivo "))
numeros=""
total=0
if(n<0):
    print("numero no permitido")
elif(n==0):
    print("el factorial es de1")
else:
    for i in range(n):
        digito=n%10
        numeros += str(i)+" + "
        total=total+i
    print("la suma de ",numeros," = ",total)