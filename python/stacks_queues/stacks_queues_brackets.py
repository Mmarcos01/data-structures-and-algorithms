from stacks_queues.stacks_queues import Stack

def validate_brackets(string):
    brackets_pair = {"}": "{", "]": "[", ")": "("}
    opening_brackets = {"{", "(", "["}
    stack = Stack()

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in brackets_pair:
            if stack.is_empty() or stack.pop() != brackets_pair[char]:
                return False

    return stack.is_empty()
