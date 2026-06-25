import string
ALPHABETS=string.ascii_lowercase

def rotate(text, key):
    key=key if key<26 else key-26
    final_string=""
    for i in range(len(text)):
        if text[i].lower() not in ALPHABETS:
            final_string+=text[i]
            continue
        new_index=ALPHABETS.index(text[i].lower())+key
        new_index=new_index if new_index<26 else new_index-26
        if text[i].isupper():
            final_string+=ALPHABETS[new_index].upper()
        else:
            final_string+=ALPHABETS[new_index]
    return final_string