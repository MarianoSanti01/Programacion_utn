import sys
path=sys.path[0]
splited_path=path.split("/")
splited_path.pop()
current_path='/'.join(splited_path)
sys.path.append(current_path)

from functions.numbers_addition import *

def test_dni_verification():
    assert dni_verification(44904987) == True
    assert dni_verification(4490498) == True
    assert dni_verification(449049) == False
    assert dni_verification(449049871) == False
def test_long_last_word():
    assert long_last_word("hola mundo")==5
    assert long_last_word("the batman")==6
def test_individual_token():
    assert individual_token("juan cruz","berrios","44904987")=="jucrbe44"
    assert individual_token("juan","berrios","44904987")=="jube44"
    assert individual_token("juan cruz lol","berrios","44904987")==""
    assert individual_token("jua cruz","berrios lol","44904987")==""
def test_multiple():
    assert multiple(4,2)==False
    assert multiple(4,3)==False
    assert multiple(2,4)==True
def test_middle_temp():
    assert middle_temp(28,15)==13
def test_phrase_with_spaces():
    assert phrase_with_spaces("hola mundo")=="h o l a m u n d o "
def test_lowest_biggest():
    assert lowest_biggest([28,15,17,19,1,100])==[100,1]
    assert lowest_biggest([-5,10,14,17,5000,100])==[5000,-5]
def test_circuferance_data():
    assert circuferance_data(25)==["1963.5","50"]
    assert circuferance_data(25.5)==["2042.82","51.0"]
def test_loggin():
    assert loggin("asaasa","asasa") == False
    assert loggin("usuario","asdasd") == False
    assert loggin("usuario1","asda") == False
    assert loggin("usuario1","asdasd") == True
def test_discount():
    assert discount({"modulo":[12000,25],"pin":[500,5],"glass":[4000,30]})==[9000,475,2800]
    assert discount({"placa madre":[58000,30],"RAM":[28000,15],"cpu":[60000,40]})==[40600,23800,36000]
def test_called():
    assert called([1,5])==5
    assert called([5,4])==20
def test_caller():
    assert caller(called,[1,2])==2
    assert caller(called,[5,4])==20
def test_create_dictionary():
    assert create_dictionary("hello friend")=={"hello":5,"friend":6}
    assert create_dictionary("")=={"":0}