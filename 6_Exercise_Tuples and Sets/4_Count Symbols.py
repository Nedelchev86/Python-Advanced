# chars = input()
# my_dict = {}
#
# for char in chars:
#     if char not in my_dict:
#         my_dict[char] = 0
#     my_dict[char] += 1
#
#
# for key, value in sorted(my_dict.items()):
#     print(f"{key}: {value} time/s")


# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")


text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")
