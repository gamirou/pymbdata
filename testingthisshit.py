from pymb import Queue, HashTable

queue = Queue()
queue.enqueue(4, 5, 6)
print(queue)


hash1 = HashTable()
hash1["Awesome"] = 456
q = hash1.toQueue()
q.enqueue(4, 5, 6, 7)
print(q)