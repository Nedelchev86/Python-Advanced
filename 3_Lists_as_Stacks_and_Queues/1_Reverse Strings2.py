text = list(input())
for i in range(len(text)):
    print(text.pop(), end="")


text = list(input())
while text:
    print(text.pop(), end="")
