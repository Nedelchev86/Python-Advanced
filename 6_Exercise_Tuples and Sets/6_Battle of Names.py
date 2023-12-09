num = int(input())
odd_set = set()
even_set = set()

for i in range(1, num + 1):
    name = sum([ord(x) for x in input()]) // i
    odd_set.add(name) if name % 2 != 0 else even_set.add(name)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    result = odd_set | even_set
elif odd_sum > even_sum:
    result = odd_set - even_set
else:
    result = odd_set ^ even_set
print(", ".join(str(x) for x in result))

