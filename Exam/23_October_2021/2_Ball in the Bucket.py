SIZE = 6

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for i in range(SIZE)]
total = 0

for throw in range(3):
    row, col = [int(x) for x in input().strip("()").split(", ")]

    if row < 0 or col < 0 or row >= SIZE or col >= SIZE:
        continue
    position = matrix[row][col]
    if position == "B":
        for r in range(SIZE):
            if matrix[r][col] != "B":
                total += matrix[r][col]
        matrix[row][col] = 0

if total < 100:
    print(f"Sorry! You need {100 - total} points more to win a prize.")
elif total <= 199:
    print(f"Good job! You scored {total} points, and you've won Football.")
elif total <= 299:
    print(f"Good job! You scored {total} points, and you've won Teddy Bear.")
elif total >= 300:
    print(f"Good job! You scored {total} points, and you've won Lego Construction Set.")
