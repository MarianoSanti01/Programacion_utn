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
from functions.funciones_ahorcado import *
import random
hidden_word = ""
words= ["teléfono","python","computadora"]
chosen_word = random.choice(words).lower()
auxiliar_word=chosen_word
trys=0
guess=0
hidden_word=hidde_the_word(chosen_word)
while True:
    if(trys==10 or guess==len(chosen_word)):
        print("fin del juego")
        break
    else:
        print("intento numero: ",trys+1)
        print(hidden_word)
        letter = input("ingrese una letra\n").lower()
        verified_letter=verifications(letter)
        if verified_letter:
            word_and_guess=change_hidden_word(letter,auxiliar_word,hidden_word,guess)
            hidden_word=word_and_guess[0]
            guess=word_and_guess[1]
            auxiliar_word=word_and_guess[2]
            trys += 1
final_mesagge(guess,chosen_word)