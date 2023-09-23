#aprender a usar funciones dese otra carpeta
from functions.funciones_ahorcado import *
from functions.numbers_addition import numbers_addition
#EJEMPLO

while (True):
    number=int(input("ingrese numero\n"))
    if(number==0):
        print("final")
        break
    else:
        total=numbers_addition(number)
        print(total)
print("la suma de los numeros ingresados es ",total)

#que esta mal?
'''El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5,
y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

*RESPUESTA*

Lo que esta mal es que esta usando variable fuera de la funcion en la funcion, esa es un amala practica
'''

#JUAEGO DEL AHORCADO
from functions.funciones_ahorcado import *#importo las funciones
import random
hidden_word = ""
words= ["teléfono","python","computadora"]
chosen_word = random.choice(words).lower()#la variable chosen word alamcena una palabra de wrods al azar
auxiliar_word=chosen_word
trys=0
guess=0
hidden_word=hidde_the_word(chosen_word)#esta función llena hidden_word con un numero de "_" igual al numero de letras de chosen_word
while True:
    if(trys==10 or guess==len(chosen_word)):#la unica manera de acabar con el while es si se hacen 10 intentos o se adivina la palabra
        print("fin del juego")
        break
    else:
        print("intento numero: ",trys+1," de 10")#se le dice al usuario su intento actual
        print(hidden_word)#se muestra con las letras que adivino y las que no un "_" en su lugar
        letter = input("ingrese una letra\n").lower()#el usuario ingresa una letra y se convierte a minuscula
        verified_letter=verifications(letter)#esta funcion verifica que se ingrese una letra, y solo caracteres del abecedario o vocales con acento
        if verified_letter:#si la verfificacion previa se cumple:
            word_and_guess=change_hidden_word(letter,auxiliar_word,hidden_word,guess)#esta funcion almacena en la variable world_and_guess una lista con distintos valores
            hidden_word=word_and_guess[0]#hidden_world se convierte en el string proveido por la lista de la función anterior
            guess=word_and_guess[1]#el numero de aciertos se convierte el numero proveido por la funcion anterior
            auxiliar_word=word_and_guess[2]#auxiliar_word es la palabra con los caracteres adivinados eliminados proviene de "change_hidden_word" esto evita que al ingresar simpre la misma letra no suban los aciertos
            trys += 1#solo aumenta el contador de intentos si el caracter es valido, para no contar con si se ingresan dos teclas por error
final_mesagge(guess,chosen_word)#dependendiend de el resultado obtenido se mustra distintos mensajes