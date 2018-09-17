import sys
sys.path.insert(0, r'.\pymb')
from linkedlist import *

linked = LinkedList()
linked.insert(7)
linked.insert(2)
print(linked)

linked2 = LinkedList()
linked2.insert(3)
linked2.insert(8)
print(linked2)

linked3 = linked.merge(linked2)
print(linked3)