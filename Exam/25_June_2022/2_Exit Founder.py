player1, player2 = input().split(", ")
SIZE = 6

matrix = [input().split() for _ in range(SIZE)]

need_rest = {
    player1: False,
    player2: False
}

while True:
    c_row, c_col = [int(x) for x in input().strip("()").split(", ")]
    position = matrix[c_row][c_col]

    if need_rest[player1]:
        need_rest[player1] = False
        player1, player2 = player2, player1
        continue

    if position == "E":
        print(F"{player1} found the Exit and wins the game!")
        break
    elif position == "T":
        print(F"{player1} is out of the game! The winner is {player2}.")
        break
    elif position == "W":
        print(F"{player1} hits a wall and needs to rest.")
        need_rest[player1] = True

    player1, player2 = player2, player1

