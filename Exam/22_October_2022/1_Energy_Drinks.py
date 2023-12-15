from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))
maximum = 300
stamat_caffeine = 0

while caffeine and energy_drinks:
    c_caffeine = caffeine.pop()
    energy = energy_drinks.popleft()
    total = c_caffeine * energy
    if maximum >= stamat_caffeine + total:
        stamat_caffeine += total
    else:
        energy_drinks.append(energy)
        if stamat_caffeine - 30 >= 0:
            stamat_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")