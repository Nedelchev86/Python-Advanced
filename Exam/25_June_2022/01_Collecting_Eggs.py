from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))
box = []

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    elif egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    paper = papers.pop()

    total = egg + paper
    if total <= 50:
        box.append(total)

print(f"Great! You filled {len(box)} boxes." if len(box) != 0 else "Sorry! You couldn't fill any boxes!")
if eggs:
    print(F"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(F"Pieces of paper left: {', '.join(str(x) for x in papers)}")
