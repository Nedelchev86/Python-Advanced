# unique_name = set()
#
# for _ in range(int(input())):
#     unique_name.add(input())
# print(*unique_name, sep="\n")


# unique_name = {input() for _ in range(int(input()))}
# print(*unique_name, sep="\n")


print(*{input() for _ in range(int(input()))}, sep="\n")