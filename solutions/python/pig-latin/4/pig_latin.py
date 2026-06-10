VOWELS=["a", "e", "i", "o", "u"]
def translate(text):
    string_space=" " in text
    if string_space:
        starting_space=0
        final_text=""
        for index, i in enumerate(text):
            if i.isspace() or index==len(text)-1:
                new_text=pig_latin_helper(text[starting_space:index+1])
                new_text+="ay "
                final_text+=new_text
                starting_space=index
        return final_text.strip()
    else:
        new_text=pig_latin_helper(text)
        new_text+="ay"
        return new_text

def pig_latin_helper(text):
    text=text.lower()
    text=text.strip()
    first_vowel_index, qu_index, y_index = index_calculater(text)
    if text[0] in VOWELS or text[0:2]=="xr" or text[0:2]=="yt":
        return text
    elif text[0] not in VOWELS:
        if "qu" in text and qu_index<first_vowel_index:
            return text[qu_index+2:]+text[0:qu_index+2]
        elif "y" in text and text[0]!="y" and y_index<first_vowel_index:
            return text[y_index:]+text[0:y_index]
        else:
            return text[first_vowel_index:]+text[0:first_vowel_index]

def index_calculater(text):
    first_vowel_index=9999999
    qu_index=9999999
    y_index=9999999
    if "qu" in text:
        qu_index=text.index("qu")
    if "y" in text:
        y_index=text.index("y")
    for index in enumerate(text):
        if text[index[0]] in VOWELS:
            first_vowel_index=index[0]
            break
    return first_vowel_index, qu_index, y_index