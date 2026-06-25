import string
lowercase_alphabets=string.ascii_lowercase
def is_pangram(sentence):
    sentence=sentence.lower()
    for letter in lowercase_alphabets:
        if letter in sentence:
            continue
        return False
    return True