'''Collatz Conjecture'''
def steps(number):
    '''Returns the number of steps a number requires to reach 1 using the rules of collatz conjecture.'''
    count=0
    if number<1:
        raise ValueError("Only positive integers are allowed")
    while number!=1:
        count+=1
        if number%2==0:
            number/=2
        else:
            number=(number*3)+1
    return count