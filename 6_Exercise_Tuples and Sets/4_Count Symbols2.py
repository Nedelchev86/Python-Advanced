some_string = input()

for el in sorted(set(some_string)):
    print(f"{el}: {some_string.count(el)} time/s")
