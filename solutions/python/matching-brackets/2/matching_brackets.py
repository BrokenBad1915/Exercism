def is_paired(input_string):
    open_brackets=["(", "{", "["]
    closed_brackets=[")", "}", "]"]
    bracket_stack=[]
    for bracket in input_string:
        if bracket in open_brackets:
            bracket_stack.append(bracket)
        elif bracket in closed_brackets:
            if not bracket_stack or open_brackets.index(bracket_stack[-1])!=closed_brackets.index(bracket):
                return False
            bracket_stack.pop()
    return not bracket_stack