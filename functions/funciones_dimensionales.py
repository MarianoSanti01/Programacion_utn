def add_two_elements_in_tupla(element1,element2):
    tupla=()
    tupla+=(element1,element2)
    return tupla
def add_three_elements_in_tupla(element1,element2,element3):
    tupla=()
    tupla+=(element1,element2,element3)
    return tupla
def find_tuple_in_list(lis,to_search):
    condition=0
    for i in lis:
        for j in i:
            if(j in to_search):
                condition=1
    if condition!=0:
        return True
    else:
        return False
def give_element_in_tupla(lis,to_search,index):
    data=[]
    for i in lis:
        for j in i:
            if(j in to_search):
                data.append(i[index])
    return data
def count_in_list_tuple(lis,to_search):
    counter=0
    for i in lis:
        for j in i:
            if j in to_search:
                counter+=1
    return counter