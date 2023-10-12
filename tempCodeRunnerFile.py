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