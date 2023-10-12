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
