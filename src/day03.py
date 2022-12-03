from curses.ascii import isupper
from re import X
from util import parse_input

def char_val(c):
    return ord(c) - 64 + 26 if isupper(c) else ord(c) - 96

def answer_1(input):
    sum = 0
    for items in input:
        half = len(items)//2
        left = set(items[0:half])
        right = set(items[half:])
        
        shared = left & right
        sum += char_val(shared.pop())
    return sum
         
def answer_2(input):
    sum = 0
    for i in range(0, len(input), 3):
        a = set(input[i])
        b = set(input[i+1])
        c = set(input[i+2])

        shared = a & b & c
        sum += char_val(shared.pop())
    return sum

def parser(lines):
    return lines

input = parse_input(parser, "input")
test = parse_input(parser, "test_input")

print(answer_1(test))
print(answer_1(input))
print(answer_2(test))
print(answer_2(input))