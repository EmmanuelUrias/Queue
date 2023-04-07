from collections import deque

queue = deque()

queue.appendleft(131.10)
queue.appendleft(131.12)
queue.appendleft(135)

print(queue)
print(queue.pop())
print(queue.pop())
