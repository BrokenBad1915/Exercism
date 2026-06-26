SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if len(list_one)==len(list_two):
        return EQUAL if list_one==list_two else UNEQUAL
    elif len(list_one)>len(list_two):
        if len(list_two)==0:
            return SUPERLIST
        else:
            if value_checker(list_one, list_two):
                return SUPERLIST
            return UNEQUAL
    elif len(list_one)<len(list_two):
        if len(list_one)==0:
            return SUBLIST
        else:
            if value_checker(list_two, list_one):
                return SUBLIST
            return UNEQUAL

def value_checker(larger_list, smaller_list):
    new_list=[]
    for larger_index, j in enumerate(larger_list):
        if smaller_list[0]==j:
            if larger_index+len(smaller_list)-1<=len(larger_list):
                for num in range(len(smaller_list)):
                    new_list.append(larger_list[larger_index+num])
                if new_list==smaller_list:
                    return True
                else:
                    new_list=[]
                    continue
            else:
                return False
        else:
            continue
