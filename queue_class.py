from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


queue = Queue()

queue.enqueue({
    'company': 'Walmart',
    'timestamp': '15 apr, 11:01 AM',
    'price': 131.10
})
queue.enqueue({
    'company': 'Walmart',
    'timestamp': '15 apr, 11:01 AM',
    'price': 131.12
}
)
queue.enqueue({
    'company': 'Walmart',
    'timestamp': '15 apr, 11:01 AM',
    'price': 135
}
)


print(queue.buffer)
print(queue.dequeue())
