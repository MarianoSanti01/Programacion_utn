#ejercisio 1
init_value= 0
while init_value<=30:
  init_value += 1
  if(init_value == 4) or (init_value == 6) or (init_value==10):
    print('The value ', init_value, ' of init_value was skipped')
    continue
  print('The value of the loop is: ', init_value)
  if(init_value==15):
    break
#ejercisio 2
while True:
  line=input("ingrese linea o deje en blanco para terminar")
  if (line == ""):
    break
  print(line.upper())
#ejercisio 3
total = 0
print(
    "D para deposito / R para retiro + la cantidad o una linea vacia para terminar la vitacora"
)
while True:
  value = input()
  if value == "":
    break
  list_values = value.split(" ")
  operation = list_values[0].upper()
  if (operation == "D"):
    total += int(list_values[1])
  elif(operation == "R"):
    total -= int(list_values[1])
print(total)
print(" ")
#ejercisio 4
while True:
  number = int(input("ingrese numero "))
  counter = 0
  if (number == 0):
    break
  for i in range(number):
    if (number % (i+1) == 0):
      counter += 1
  if (counter == 2):
    print("numero ingresado es primo")
  else:
    print("numero ingresado no es primo")
print("final")
#ejercisio 5

years=input("ingrese dos años")
years_list=years.split(" ")

if ((int(years_list[0]) - int(years_list[1])) >0):
  first=int(years_list[0])
  second=int(years_list[1])
else:
  first=int(years_list[1])
  second=int(years_list[0])
while second<=first:
  if (second % 4 != 0):
    second += 1
    continue
  else: 
    if (second % 400 == 0) and (second % 100 == 0):
      print (second)
    elif (second % 100 != 0):
      print (second)
    second += 1
#EJERCISIO 6
for i in range(20):
  if ((i+1)%2!=0):
    continue
  else:
    print(i+1)
#EJERCISIO 7
list=[1,2,3,4,5,6,7,8,9]
number=int(input("ingrese un numero del 1 al 9 "))
if (number>9):
  print("numero no valido")
for i in list:
  if(number == list[i-1]):
    print("el numero, ", number ," esta en la posicion ",i-1)
    break
#EJERCISIO 8
operation=int(input("ingrese operacion 1,2,3 o 0 para salir "))
while True:
  if operation==0:
    print("fin")
    break
  elif (operation==1):
    print("operacion 1 ejecutada")
  elif (operation==2):
    print("operacion 2 ejecutada")
  elif (operation == 3):
    print("operacion 3 ejecutada")
  else:
    print("esa operacion no es valida")
  operation=int(input("ingrese operacion 1,2,3 o 0 para salir "))