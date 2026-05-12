import re
import sys
import operator
import pprint as pretty_print

pprint = lambda obj: pretty_print.PrettyPrinter(indent=4).pprint(obj)

def fail(s):
    print(s)
    sys.exit(-1)

class InterpreterObject(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

class Symbol(InterpreterObject):
    pass

class String(InterpreterObject):
    pass

class Lambda(InterpreterObject):
    def __init__(self.arguments, code):
        self.arguments = arguments
        self.code = code

    def __repr__(self):
        return f"(lambda ({self.arguments}) ({self.code})"

# Parser
def tokenize(s):
    ret = []
    in_string = False
    current_word = ''

    for i, char in enumerate(s):
        if char == "'":
            if in_string is False:
                in_string = True
                current_word += char
            else:
                in_string = False
                current_word += char
                ret.append(current_word)
                current_word = ''

        elif in_string is True:
            current_word += char
        
        elif char in ['\t', '\n', ' ']:
            continue

        elif char in ['(', ')']:
            ret.append(char)

        else:
            current_word += char
            if i < len(s) - 1 and s[i+1] in ['(', ')', ' ', '\n', '\t']:
                ret.append(current_word)
                current_word = ''
    return ret

# Utility functions that convert tokens to their actual values
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_string(s):
    if s[0] == "'" and s[-1] == "'":
        return True
    return False

def parse(tokens):
    itert = iter(tokens)
    token = itert.next()

    if token != '(':
        fail("Unexpected token {}".format(token))

base_environment = {
    'print': lambda x: sys.stdout.write(str(x) + '\n')
}


def main():
    s = 'abc'
    tokenize(s)

if __name__ == '__main__':
    main()
