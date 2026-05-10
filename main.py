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

base_environment = {
    'print': lambda x: sys.stdout.write(str(x) + '\n')
}


def main():
    s = 'abc'
    tokenize(s)

if __name__ == '__main__':
    main()
