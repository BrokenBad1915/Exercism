'''The code calculates the total number of grains the servant is to be rewarded. The code also helps you evaluate the number of grains present on a particular sqaure.'''
def square(number):
    if number==1:
        return number
    if 1<number<=64:
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")

def total():
    return (2**64)-1