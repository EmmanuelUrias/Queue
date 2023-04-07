from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if self.is_empty():
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_order_queue = Queue()


def place_orders(orders):
    for order in orders:
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while food_order_queue.is_empty() == False:
        order = food_order_queue.dequeue()
        print("Now serving: ", order)
        time.sleep(1)


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger',
              'pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
