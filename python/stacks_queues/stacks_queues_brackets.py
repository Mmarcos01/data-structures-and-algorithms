from stacks_queues.stacks_queues import Stack

# ======== Validate Brackets ========

def validate_brackets(string):
    brackets_pair = {"}": "{", "]": "[", ")": "("}
    opening_brackets = {"{", "(", "["}
    stack = Stack()

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in brackets_pair:
            if stack.isEmpty() or stack.pop() != brackets_pair[char]:
                return False

    return stack.isEmpty()

# def validate_brackets(string):
#     open_brackets = ["[","{","("]
#     closed_brackets = ["]","}",")"]
#     stack = Stack()
#     for bracket in string:
#         if bracket in open_brackets:
#             stack.push(bracket)
#         elif bracket in closed_brackets:
#             pos = closed_brackets.index(bracket)
#             if ((len(stack) > 0) & (open_brackets[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False

