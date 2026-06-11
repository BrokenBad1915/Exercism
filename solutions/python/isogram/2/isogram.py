'''Checking if a particular string is an Isogram or not'''
import string
ALPHABETS=string.ascii_lowercase
def is_isogram(q_string):
    letter_list=[]
    q_string=q_string.lower()
    for letter in q_string:
        if letter not in letter_list and letter in ALPHABETS:
            letter_list.append(letter)
            print(letter_list)
            continue
        elif letter in letter_list:
            return False
    return True