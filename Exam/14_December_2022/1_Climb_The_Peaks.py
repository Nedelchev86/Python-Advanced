from collections import deque

portions = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))

success = []

peaks = deque([
    (80, "Vihren"),
    (90, "Kutelo"),
    (100, "Banski Suhodol"),
    (60, "Polezhan"),
    (70, "Kamenitza"),
])

while portions and stamina and peaks:
    c_portions = portions.pop()
    c_stamina = stamina.popleft()
    total = c_portions + c_stamina

    first_peak = peaks.popleft()

    if total >= first_peak[0]:
        success.append(first_peak[1])
    else:
        peaks.appendleft(first_peak)

if len(success) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if success:
    print("Conquered peaks:")
    print(*success, sep="\n")