def numbers_addition(number):
    result = 0
    while number>0:
        digit=(number%10)
        result += digit
        number=int(number/10)
    return result