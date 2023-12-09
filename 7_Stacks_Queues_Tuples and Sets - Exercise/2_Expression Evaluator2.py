from collections import deque
from functools import reduce

sequence = deque(int(x) if x.isdigit() else x for x in input().split())
current_nums = []

while sequence:
    element = sequence.popleft()

    if element == "+":
        sequence.appendleft(reduce(lambda a, b: a+b, current_nums))
        current_nums = []
    elif element == "-":
        sequence.appendleft(reduce(lambda a, b: a-b, current_nums))
        current_nums = []
    elif element == "*":
        sequence.appendleft(reduce(lambda a, b: a*b, current_nums))
        current_nums = []
    elif element == "/":
        sequence.appendleft(reduce(lambda a, b: a/b, current_nums))
        current_nums = []
    else:
        current_nums.append(int(element))
print(round(element))
