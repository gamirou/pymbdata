from hashtable import HashTable
from linkedlist import LinkedList
from others import Stack

hash1 = HashTable()
hash1.insert("George", 23)
hash1.insert("Egorge", 14)
hash1.insert("Fforge", 12)
hash1.insert("Hdorge", 15)

hash1.insert("Love", 25)
hash1.insert("Hate", 16)

hash2 = HashTable()
hash2.insert("Kovf", 32)
hash2.insert("Ibte", 56)

hash3 = hash1.merge(hash2)
print("Hash 1: ")
print(hash1)
print("Hash 2: ")
print(hash2)
print("Hash 3: ")
print(hash3)

print("All sorted linked lists inside hash 1")
allLists = hash1.getList()
for linkedList in allLists:
    print(linkedList)

print()

print("Hash 3 to Stack: ")
stack = hash3.toStack("values")
print("Original stack")
print(stack)

valPoppedStack1 = stack.pop()
valPoppedStack2 = stack.pop()
print("The values {} and {} have been popped".format(valPoppedStack1, valPoppedStack2))
print("The new stack is: {}\n".format(stack))

print("Hash 2 to Queue: ")
queue = hash2.toQueue()
print("Original queue")
print(queue)

valPoppedQueue = queue.dequeue()
print("The value {} has been popped".format(valPoppedQueue))
print("The new queue is: {}\n".format(queue))

print("Hash 1 to Binary Tree")
binaryTree = hash1.toBST()
binaryTree.showSorted()