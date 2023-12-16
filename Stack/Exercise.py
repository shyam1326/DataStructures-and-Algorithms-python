

# 1. Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.

# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from stack import Stack

def reverse_string(string):
    obj = Stack()

    for i in string:
        obj.push(i)

    rev = ''
    while obj.size() != 0:
        rev += obj.pop()
    
    print(rev)

# 2. Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

def match(s):
    match_string = {
        ')':'(', 
        '}': '{',
        ']':'['
    }
    return match_string[s]

def is_balanced(string):
    obj = Stack()

    for i in string:
        if i in ['(', '{', '[']:
            obj.push(i)
        elif i in [')', '}', ']']:
            if obj.size() == 0:
                return False
            else:
                if match(i) != obj.pop():
                    return False
    return obj.size() == 0



if __name__=="__main__":
    # reverse_string("We will conquere COVID-19")
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))