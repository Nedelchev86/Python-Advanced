from collections import deque

int_Stack = input().split()
reversed_stack = []
for i in range(len(int_Stack)):
    reversed_stack.append(int_Stack.pop())
print(" ".join(reversed_stack))


int_Stack = deque(input().split())

for i in range(len(int_Stack)):
    print(int_Stack.pop(), end=" ")




int_Stack = input().split()
while int_Stack:
    print(int_Stack.pop(), end=" ")
