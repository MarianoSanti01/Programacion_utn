from functions.numbers_addition import *
numbers=[]
while True:
    num=int(input("ingrese un numero primo o un numero no primo para terminar\n"))
    is_prime=is_prime_number(num)
    if not is_prime:
        print("FIN")
        break
    else:
        while True:
            digit=int(input("ingrese un digito\n"))
            digit_condition=sigle_digit_verification(digit)
            if not digit_condition:
                print("el digito debe ser solo un numero, vuelva a ingresarlo")
            else:
                counter=digit_times_in_number(num,digit)
                digits_sum=numbers_addition(num)
                print("el digito ingresado ",digit," se repite en el numero ",num,counter," veces")
                print("la suma de los digitos de ", num," es ",digits_sum)
                numbers.append(num)
                break
biggest=lowest_biggest(numbers)
total=1
biggest_factorial=facorial(biggest[0],total)
print("el mayor numero ingresado fue ",biggest[0]," y su factorial es ",biggest_factorial)