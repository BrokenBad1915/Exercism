def is_armstrong_number(num):
    number_of_digits=len(str(num))
    original_num=num
    final_num=0
    while num>0:
        final_num+=((num%10)**number_of_digits)
        num=num//10
    if final_num==original_num:
        return True
    return False
