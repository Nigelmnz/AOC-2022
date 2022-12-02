# from util import parse_input

# def rps(them, me):
#     score = me + 1

#     if them == me:
#         score += 3
#     elif (them + 1) % 3 == me:
#         score += 6

#     return score
    
# def rps2(them, me):
#     if me == 0:
#         return rps(them, (them - 1) % 3)
#     elif me == 1:
#         return rps(them, them)
#     else:
#         return rps(them, (them + 1) % 3)  

# def answer_1(input):
#     return sum([rps(them, me) for them, me in input])
         
# def answer_2(input):
#     return sum([rps2(them, me) for them, me in input])

# def translate(move):
#     moveset = "ABC" if move in "ABC" else "XYZ"
#     return [0,1,2][moveset.index(move)]

# def parser(lines):
#     return [[translate(move) for move in line.split(" ")] for line in lines]

# input = parse_input(parser, "input")
# test = parse_input(parser, "test_input")

# print(answer_1(test))
# print(answer_1(input))
# print(answer_2(test))
# print(answer_2(input))