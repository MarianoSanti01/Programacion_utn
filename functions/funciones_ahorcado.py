alphabet="abcdefghijklmnñopqrstuvwxyzáéíóú"
def verifications(letter):
    if (len(letter) != 1) or (letter not in alphabet) :
        print("------dato no valido ingrese una letra------")
    else:
        return True
def hidde_the_word(word):
    word2=""
    for i in word:
        i="_"
        word2 += i
    return word2
def change_hidden_word(letter,word,hidden_word,guess):
    if letter in word:
        index=0
        for i in word:
            if (i==letter):
                lis_word=list(hidden_word)
                lis_word[index]=letter
                hidden_word=""
                hidden_word=hidden_word.join(lis_word)
                guess +=1
                word=word.replace(word[index],"_",1)
            index +=1
        new_word=[hidden_word,guess,word]
        print("letra correcta")
        return new_word
    else:
        new_word=[hidden_word,guess,word]
        print("letra incorrecta")
        return new_word
def final_mesagge(guess,chosen_word):
    if(guess==len(chosen_word)):
        return print("ganaste la pabra secreta era ",chosen_word)
    else:
        return print("perdiste la palbra secreta era ",chosen_word)