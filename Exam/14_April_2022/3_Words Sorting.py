def words_sorting(*args):
    words_dict = {}
    total_sum = 0

    for el in args:
        words_dict[el] = sum(ord(x) for x in el)
        total_sum += words_dict[el]

    sorted_dict = sorted(words_dict.items(), key=lambda x: -x[1] if total_sum % 2 != 0 else x[0])
    result = [F"{key} - {value}" for key, value in sorted_dict]

    return "\n".join(result)

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))