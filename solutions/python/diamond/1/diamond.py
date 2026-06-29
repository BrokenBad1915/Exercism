import string
CAPITAL_LETTERS=string.ascii_uppercase
def rows(letter):
    my_num=CAPITAL_LETTERS.index(letter)+1
    pattern_list=[]
    for i in range(0, my_num*2-1):
        row_list=[]
        for j in range(1, my_num*2):
            if i<my_num and (j==my_num+i or j==my_num-i):
                row_list.append(CAPITAL_LETTERS[i])
            elif i>=my_num and (j==my_num-(my_num*2-2-i) or j==my_num+(my_num*2-2-i)):
                row_list.append(CAPITAL_LETTERS[my_num-(i-my_num)-2])
            else:
                row_list.append(" ")
        pattern_list.append("".join(row_list))
    return pattern_list