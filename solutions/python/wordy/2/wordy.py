OPERATION_DICT={"plus": lambda num1, num2: num1+num2,
                    "minus": lambda num1, num2: num1-num2,
                    "multiplied": lambda num1, num2: num1*num2,
                    "divided": lambda num1, num2: num1/num2}
def answer(question):
    question=question.replace("?", "")
    question_list=question.split(" ")
    while "by" in question_list: question_list.remove("by")
    result=0
    for index, value in enumerate(question_list):
        if value.isdigit() or value[0]=="+" or value[0]=="-":
            if index==len(question_list)-1:
                if result==0:
                    return int(float(value))
                return int(float(result))
            elif question_list[index+1] in OPERATION_DICT and index+2!=len(question_list):
                if result==0:
                    result=value
                result=operation_calculator([result]+question_list[index+1:index+3])
            else:
                if question_list[index+1] not in OPERATION_DICT and not question_list[index+1].isdigit():
                    raise ValueError("unknown operation")
                else:
                    raise ValueError("syntax error")
        elif index==len(question_list)-1 and result==0:
            raise ValueError("syntax error")

def operation_calculator(operation_list):
    integer_occurance=0
    operation_occurance=0
    for i in operation_list:
        if i.isdigit() or i[0]=="+" or i[0]=="-": integer_occurance+=1
        elif i in OPERATION_DICT: operation_occurance+=1
    if integer_occurance==2 and operation_occurance==1:
        current_answer=OPERATION_DICT[operation_list[1]](int(float(operation_list[0])), int(float(operation_list[2])))
        return f"{int(float(current_answer))}"
    raise ValueError("syntax error")