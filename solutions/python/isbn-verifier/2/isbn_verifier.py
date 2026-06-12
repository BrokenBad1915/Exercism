def is_valid(isbn):
    string_without_hyphen=""
    count=10
    result=0
    string_without_hyphen=list(isbn.replace("-", ""))
    if len(string_without_hyphen)!=10: return False
    else:
        for num in string_without_hyphen:
            try:
                final_num=int(num)
                result+=final_num*count
                count-=1
            except ValueError:
                if num=="X":
                    result+=10
                else:
                    return False
    if result%11==0:
        return True
    return False