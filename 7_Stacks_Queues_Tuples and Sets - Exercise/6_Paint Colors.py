from collections import deque

substrings = deque(input().split())

main_color = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}
collected_color = []

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ""

    result = first + second

    if result in main_color or result in secondary_colors:
        collected_color.append(result)
        continue

    result = second + first
    if result in main_color or result in secondary_colors:
        collected_color.append(result)
        continue

    first = first[:-1]
    second = second[:-1]

    if first:
        substrings.insert(len(substrings) // 2, first)
    if second:
        substrings.insert(len(substrings) // 2, second)

result = []

# required_color = {
#     'orange': ['red', 'yellow'],
#     'purple': ["red", 'blue'],
#     'green': ['yellow', 'blue'],
# }

for color in collected_color:
    if color in main_color:
        result.append(color)
    else:
        if color == "orange":
            if "red" in collected_color and "yellow" in collected_color:
                result.append("orange")
        elif color == 'purple':
            if "red" in collected_color and "blue" in collected_color:
                result.append("purple")
        elif color == 'green':
            if "yellow" in collected_color and "blue" in collected_color:
                result.append("green")
print(result)
