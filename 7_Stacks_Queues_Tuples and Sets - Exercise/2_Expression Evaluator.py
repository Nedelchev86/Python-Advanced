from collections import deque

input_data = input().split()
numbers = deque()
result = 0

for el in input_data:
    if el in "+-/*":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            if el == "+":
                result = first + second
            elif el == "-":
                result = first - second
            elif el == "/":
                result = first // second
            else:
                result = first * second
            numbers.appendleft(result)
    else:
        numbers.append(int(el))
print(result)
