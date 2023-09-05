#ejercisio 1
'''init_value= 0
while init_value<=30:
  init_value += 1
  if(init_value == 4) or (init_value == 6) or (init_value==10):
    print('The value ', init_value, ' of init_value was skipped')
    continue
  print('The value of the loop is: ', init_value)
  if(init_value==15):
    break'''
#ejercisio 2
'''while True:
  line=input("ingrese linea o deje en blanco para terminar")
  if (line == ""):
    break
  print(line.upper())'''
#ejercisio 3
'''total = 0
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
print(" ")'''
#ejercisio 4
'''while True:
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
print("final")'''
#ejercisio 5


'''inicio
leer año1, año2
escribir años entre año1 y año2 que sean bisiestos'''
years=input("ingrese dos años")
years_list=years.split(" ")

if ((int(years_list[0]) - int(years_list[1])) >0):
  first=int(years_list[0])
  second=int(years_list[1])
else:
  first=int(years_list[1])
  second=int(years_list[0])
while second<first:
  if (second % 4 == 0):
    if (second % 400 == 0) and (second % 100 == 0):
      print (second)
    elif (second % 100 != 0):
      print (second)
  second += 1
