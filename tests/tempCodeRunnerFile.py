import sys

sys.path.append("C:/Users/juanc/Desktop/Programacion_utn/functions")

from functions.numbers_addition import *
def test_dni_verification():
    assert dni_verification(44904987) == True