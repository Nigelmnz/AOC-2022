from typing import List

from util import parse_input

def answer_1(input: List[int]):
    increases = 0
    for i, depth in list(enumerate(input))[1:]:
        if depth > input[i-1]:
            increases += 1
    return increases

def answer_2(input: List[int]):
    window_inputs = [sum(input[i:i+3]) for i in range(0, len(input)-2)]
    return answer_1(window_inputs)

def parser(lines) -> List[int]:
    return [int(n) for n in lines]

input = parse_input(parser, "day01")
print(answer_1(input))
print(answer_2(input))