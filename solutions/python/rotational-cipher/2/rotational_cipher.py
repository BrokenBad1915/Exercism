'''Caesor cipher'''
import string
ALPHABETS=string.ascii_lowercase

def rotate(text, key):
    '''Implementing caesor cipher encoding part'''
    key=key if key<26 else key-26
    final_string=""
    for alph in text:
        if alph.lower() not in ALPHABETS:
            final_string+=alph
            continue
        new_index=ALPHABETS.index(alph.lower())+key
        new_index=new_index if new_index<26 else new_index-26
        if alph.isupper():
            final_string+=ALPHABETS[new_index].upper()
        else:
            final_string+=ALPHABETS[new_index]
    return final_string