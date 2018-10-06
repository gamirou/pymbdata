import pymb

queue = pymb.queue()
queue.enqueue(5, 4, 3, 2, 5, "abc")
print(queue.dequeue())
print(queue)
print(queue.items)