#ejercisio 1
palabra_encriptada =""
abecedario="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("¿cual es el corrimiento? "))
palabra=""
for i in range(1):
  palabra = input("ingrese el mensaje ")
  for letra in palabra:
    if (letra in abecedario):
      indice = abecedario.find(letra)
      indice_encriptado = (indice+corrimiento)%27
      palabra_encriptada += abecedario[indice_encriptado]
    else:
      palabra_encriptada += letra


  print(palabra_encriptada)
  #ejercisio 2
  ''' Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.'''

n = 1
dig_pares = 0
dig_inpares = 0
while n != 0:
  n = int(input("INGRESE UN NUMERO par postivo "))
  if (n % 2 != 0):
    print("numero no valido")
  else:
    auxiliar = n
    dig_pares_p = 0
    dig_inpares_p = 0
    while auxiliar > 0:
      digito = auxiliar % 10
      if (digito % 2 == 0):
        dig_pares = dig_pares + 1
        dig_pares_p = dig_pares_p + 1
      else:
        dig_inpares_p = dig_inpares_p + 1
        dig_inpares = dig_inpares + 1
      auxiliar = auxiliar / 10
    print("hay ", dig_pares_p, " pares y ", dig_inpares_p, " inpares")
print("hay ", dig_pares, " pares y ", dig_inpares, " inpares")
