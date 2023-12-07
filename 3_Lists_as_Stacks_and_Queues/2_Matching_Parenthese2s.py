data = input()
my_Stack = []
for i in range(len(data)):
    index = data[i]
    if index  == "(":
        my_Stack.append(i)
    elif index == ")":
        print(data[my_Stack.pop():i +1])


