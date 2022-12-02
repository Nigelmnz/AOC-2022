from util import parse_input

def answer_1(input):
    return max(input)

def answer_2(input):
    return sum(sorted(input, reverse=True)[0:3])

def parser(lines):
    counts = []
    counter = 0
    for line in lines:
        if line == "":
            counts.append(counter)
            counter = 0
        else:
            counter += int(line)

    return counts + [counter]

input = parse_input(parser, "input")
test = parse_input(parser, "test_input")

print(answer_1(test))
print(answer_1(input))
print(answer_2(input))