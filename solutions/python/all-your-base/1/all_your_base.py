'''Converting integers from one type of base to another'''
def rebase(input_base, digits, output_base):
    if input_base<=1:
        raise ValueError("input base must be >= 2")
    elif output_base<=1:
        raise ValueError("output base must be >= 2")
    current_number=result_finder(input_base, digits)
    converted_number=base_convertor(output_base, current_number)
    return converted_number
    
def result_finder(base, list_sequence):
    result=0
    for index, num in enumerate(list_sequence):
        if 0>num or num>=base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        result+=num*(base**(len(list_sequence)-index-1))
    return result

def base_convertor(required_base, number):
    result=[]
    count=0
    while True:
        result.insert(0, number%required_base)
        if number//required_base==0:
            return result
        number=number//required_base
        count+=1