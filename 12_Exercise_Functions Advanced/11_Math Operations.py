from collections import deque


def math_operations(*args, **kwargs):

    numbers = deque(args)
    while numbers:
        number = numbers.popleft()
        kwargs["a"] += number
        if not numbers:
            break
        number = numbers.popleft()
        kwargs["s"] -= number
        if not numbers:
            break
        number = numbers.popleft()
        if number != 0:
            kwargs["d"] /= number
        if not numbers:
            break

        number = numbers.popleft()
        kwargs["m"] *= number
    sorted_dict = [F"{key}: {value:.1F}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return "\n".join(sorted_dict)


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
