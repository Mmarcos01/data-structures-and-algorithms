# ======== Validate Brackets ========

open_brackets = ["[","{","("]
closed_brackets = ["]","}",")"]

def validate_brackets(string):
    stack = []
    for bracket in string:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in closed_brackets:
            pos = closed_brackets.index(bracket)
            if ((len(stack) > 0) & (open_brackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
