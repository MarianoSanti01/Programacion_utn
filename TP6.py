#Ejercicio 1 + ejercicio 2 + ejercicio 3 + ejercicio 4 + ejercicio 5
from functions.funciones_dimensionales import *
data=[]
while True:
    num=int(input("ingrese en numero \n"))
    if num==0:
        break
    else:
        data=add_in_list(data,num)
print("datos ingresados")
show_list(data)
d_num=int(input("igrese numero para eliminar\n"))
deleate_from_list(data,d_num)
print("los datos ingresados menos el eleminado:\n",)
show_list(data)
sum_data=sum_list_elements(data)
print("la suma de los numero en la lista es ",sum_data)
num1=int(input("ingrese un numero y se filtraran todos los mayores dejando solo los que sean menores al numero ingresado\n"))
data=filter_lower_numbers_from_list(data,num1)
print(data)
data_and_counter=count_same_elements_in_list(data)
print(data_and_counter)
print("---FIN---")

#EJERCICIO 6

primary_names = []
secondary_names = []

# Solicitar nombres de estudiantes
x=2
while x != 0:
    if x ==2:
        names= input("Ingrese nombre de estudiante de primaria, ingrese una x para salir ").title()
        if names != 'X':
            primary_names.append(names)
        else:
            x-=1
            print(" ")
    elif x==1:
        names= input("Ingrese nombre de estudiante de secundaria, ingrese una x para salir ").title()
        if names != "X":
            secondary_names.append(names)
        else:
            x-=1
            print(" ")

#Imprimir nombres sin repetir
print(" ")
print("Nombres")
all_names = set(primary_names+secondary_names)
for name in all_names:
    print(name)

#Imprimir nombres repetidos
print(" ")
print("Nombres repetidos")
repeated_names= set(primary_names) & set(secondary_names)
for name in repeated_names:
    print(name)

#Imprimir nombres que no se repiten
print(" ")
print("Nombres de primaria que no se repiten en secundaria")
primary_names_no_repeat= set(primary_names) - set(secondary_names)
for name in primary_names_no_repeat:
    print(name)

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#EJERCICIO 7

ocurrency={}
string_counts=0

#Contador hasta 50 en el que pide las cadenas
while string_counts < 50:
    chain = input("Ingrese una cadena ").upper()
    string_counts +=1
    
    #Lector de caracteres y ocurrencias
    for character in chain:
        if character in ocurrency:
            ocurrency[character] +=1
        else:
            ocurrency[character]=1

print(" ")
print("Ocurrencias de caracteres en los strings")
for character, cuantity in ocurrency.items():
    print(f"'{character}': {cuantity}")

#ejercicio 11
from functions.funciones_dimensionales import *
dictionary={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa=input("ingrese la divisa a consultar\n").lower()
validation=exist_dictionary(dictionary,divisa)
if validation:
    data=search_value_in_dictionary(dictionary,divisa)
    print("el simolo de ",divisa," es ",data)
else:
    print("no se encontro la divisa ingresada")
#ejercicio 12
from functions.funciones_dimensionales import *
dictionary={}
name=input("ingrese su nombre\n").lower()
age=int(input("ingrese su edad\n"))
adrees=input("ingrese su dirección\n").lower()
dictionary=add_element_in_dictionary(dictionary,"name",name)
dictionary=add_element_in_dictionary(dictionary,"age",age)
dictionary=add_element_in_dictionary(dictionary,"adress",adrees)
print(dictionary)
#ejercicio 13
from functions.funciones_dimensionales import *
fruits={}
while True:
    fruit=input("Ingrese nombre de la fruta\n").lower()
    validation1=exist_dictionary(fruits,fruit)
    if not validation1:
        price=int(input("esa fruta no esta registrada ingrese el precio para guardarla\n"))
        fruits=add_element_in_dictionary(fruits,fruit,price)
        kg=int(input("ingrese los kilogramos\n "))
        price_given=search_value_in_dictionary(fruits,fruit)
        total=price_given*kg
    else:
        kg=int(input("ingrese los kilogramos\n "))
        price_given=search_value_in_dictionary(fruits,fruit)
        total=price_given*kg
    print("valor por kg de ",fruit," es ",price_given,"por los ",kg," kg's pedidos el total a pagar es de ",total)
