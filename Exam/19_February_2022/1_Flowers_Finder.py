from collections import deque

words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

found = False

vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    first = vowels.popleft()
    second = consonants.pop()

    for key, value in words.items():
        words[key] = words[key].replace(first, "")
        words[key] = words[key].replace(second, "")
        if len(words[key]) == 0:
            print(f"Word found: {key}")
            found = True
            break
    if found:
        break
if not found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
