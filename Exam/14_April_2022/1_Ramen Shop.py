from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls_of_ramen and customers:
    ramen = bowls_of_ramen.pop()
    customer = customers.popleft()

    if ramen > customer:
        bowls_of_ramen.append(ramen - customer)
    elif ramen < customer:
        customers.appendleft(customer - ramen)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(F"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(F"Customers left: {', '.join(str(x) for x in customers)}")