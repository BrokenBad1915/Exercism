def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    total=0
    for num in range(1, int(number**0.5)+1):
        if number%num==0:
            total+=num
            if num!=number//num:
                total+=number//num
    total-=number
    return "perfect" if total == number else "abundant" if total > number else "deficient"