import math

#EJERCISIO 1

ano_pc = int(input("Ingrese los años de su computador: "))
if ano_pc <= 2:
    print("Su computador es nuevo")
else:
    print("Su computador es viejo")

#EJERCISIO 2

ano_pc = int(input("Ingrese los años de su computador: "))
if (ano_pc <= 2) and (ano_pc >= 0) :
    print("su pc es nueva")
elif ano_pc < 0:
    print("error ")
  
#EJERCISIO 3

nombres = input("ingrese nombres separados  ")
nombres_separados = nombres.split(" ")
nombre1=nombres_separados[0]
nombre2 = nombres_separados[1]

if (nombre1[0] == nombre2[0]):
  print("hay concidencia")
else:
  print("no hay concidencia")
  
#EJERCISIO 4

voto = input("Ingrese a que candidato va a votar: ")
voto = voto.lower()
if voto == "a":
    print("Usted a votado por el partido ROJO")
elif voto == "b":
    print("Usted a votado por el partido VERDAD")
elif voto == "C":
    print("Usted a votado por el partido AZUL")
else:
    print("Opción erronea")

#EJERCISIO 5

letra = input('Ingresa un caracter: \n')
vocales = ('a','e','i','o','u')
if(len(letra) > 1):
   print('Error de entrada, ingresar solo un carácter')
else:
  if(letra in vocales):
    print(f'La letra "{letra}" es una vocal')
  else:
    print("la letra ",letra," no es una vocal")

#EJERCISIO 6

año = int(input('Ingresar año:'))
if (año % 4 == 0 and año % 100 != 0):
  print('año bisiesto')
elif (año % 4 == 0 and año % 100 != 0) and año % 400 == 0:
  print('año bisiesto')
else:
  print('año no bisiesto')

#EJERCISIO 7
print("Ingresar tres números")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
print("El número mas grande es")
max = a
if b> max:
  max = b
if c>max:
 max=c
print(max)

#EJERCISIO 8 

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if (user == "Gwenevere") and (password == "excalibur"):
  print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
  print("Acceso denegado")

#EJERCISIO 9
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

#EJERCISIO 10

edad = int(input("ingrese edad"))
if (edad <= 18 ):
  print("juega gratis")
else:
  print("debe pagar 1800")

#EJERCISIO 11

pregunta = input('¿Quieres una pizza vegetariana[1] o no vegetariana[2]?\n (Responder [1 o 2]\n')
if pregunta == '1':
  print('Ingredientes vegetarianos\n [Pimiento(1) , Tofu(2)]')
  ingrediente = input('Ingresa una opcion de ingrediente:\n')
if(ingrediente == '1'):
    ingrediente_adicional = 'Pimiemto'
    print('La pizza es vegatariana\n')
    print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
elif(ingrediente == '2'):
    ingrediente_adicional = 'Tofu'
    print('La pizza es vegatariana\n')
    print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
elif pregunta == '2':
    print('Ingredientes no vegetarianos\n [Pepperoni(1) , Jamon(2), Salmon(3)]')
if(pregunta == '2'):
    ingrediente = input('Ingresa una opcion de ingrediente:\n')
if(ingrediente == '1'):
  ingrediente_adicional = 'Pepperoni'
  print('La pizza no es vegatariana\n')
  print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
elif(ingrediente == '2'):
  ingrediente_adicional = 'Jamon'
  print('La pizza no es vegatariana\n')
  print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
elif(ingrediente == '3'):
  ingrediente_adicional = 'Salmon'
  print('La pizza no es vegatariana\n')
  print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
else:
  print('Error de entrada')

#EJERCISIO 12
fecha_actual = int(input("ingrese la fecha actual "))
fecha_aleatoria = int(input("ingrese fecha aleatoria "))
if (fecha_actual > fecha_aleatoria):
  print("pasaron ",fecha_actual-fecha_aleatoria," años desde esa fecha")
else:
  print("faltan",fecha_aleatoria-fecha_actual," años para esa fecha")

#EJERCISIO 13
num1=int(input('Ingresar numero='))
num2=int(input('Ingresar otro numero='))
if num1>0 and num2>0:
  if num1>num2:
    if num1%num2==0:
      print(f'{num1} es multiplo de {num2}')
    else:
      print(f'{num1} NO es multiplo de {num2}')
  if num2>num1:
    if num1%num2==0:
      print(f'{num2} es multiplo de {num1}')
    else: 
      print(f'{num2} NO es multiplo de {num1}')
else:
  print('Se ingresaron numeros negativos o nulos')

#EJERCISIO 14
print("Ingresar los coeficientes de una ecuacion de primer grado ax + b = 0")
a=int(input("a="))
b=input("b=")
if a==0 and b!=0:
  print("No hay solución")
elif a!=0 and b== "-x":
  print("infinitas soluciones")
elif a!=0 :
  b=int(b)
  x=-b/a
  print("la solución es x= ", x)

#EJERCISIO 15

operacion=input("desea saer el area de un triangulo(t) o de un circulo(c) ").lower()   #b*a/2
if (operacion == "c"):
  r=int(input("escriba el radio del circulo"))
  print("el area del circulo es de: ", math.pi*(r**2))
elif(operacion=="t"):
  h=int(input("ingrese la altura del triangulo "))
  b=int(input("ingrese la base del triangulo "))
  print("el area del triangul es de: ", b*h/2)
else:
  print("valor ingresado no valido ")

#EJERCISIO 16

a= int(input("Ingrese un numero entero: "))
b=int(input("Ingrese otro valor: "))
print("Ingrese la operacion que desea realizar, 1: para suma; 2: para el producto; 3: para la resta; 4: para ver la division")
operacion = (int(input()))
if operacion == 1:
   print(a +b)
elif operacion == 2:
    print(a * b)
elif operacion == 3:
    print(a - b)
elif operacion == 4:
    print(a / b)
else:
   print("Error ")

#EJERCISIO 17

dia = input("ingrese el dia de la semana ")
dia_low=dia.lower()
if (dia_low == "lunes"):
   print("hoy es lunes")
elif(dia_low=="viernes"):
   print("hoy es viernes")
elif(dia_low=="sabado" or dia=="domingo"):
    print("hoy es fin de semana")
else:
   print("hoy es martes, miercoles o jueves")

#EJERCISIO 18

horas_trabajadas=int(input('Ingresar las horas trabajadas en el mes:'))
salario_hora=int(input('Ingresar su salario por hora:'))
if horas_trabajadas>48:
  horas_extras=horas_trabajadas-48
  print(f'Las horas extras trabajadas fueron:{horas_extras}')
  salario_horas_extras=(salario_hora*0.1)+salario_hora
  salario_total=(48*salario_hora) + (horas_extras+salario_horas_extras)
  print(f'Salario total:${salario_total}')
else:
  print(f'No trabajo horas extras. Las horas trabajadas fueron:  {horas_trabajadas}')
salario_total=horas_trabajadas*salario_hora

#EJERCISIO 19

cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
precio = 60 * cant_lapiz
if cant_lapiz >= 1000:
    precio_final = precio - (precio * 0.7)
