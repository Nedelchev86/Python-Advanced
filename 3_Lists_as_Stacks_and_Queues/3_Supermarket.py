# with stack

people = []

while True:
    data = input()
    if data == "End":
        print(F"{len(people)} people remaining.")
        break
    elif data == "Paid":
        print("\n".join(people))
        people.clear()
    else:
        people.append(data)

