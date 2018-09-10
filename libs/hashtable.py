from linkedlist import LinkedList
from others import *

class HashTable:
    """Object that behaves like a hash table (almost! it is mutant >:O)"""
    TABLE_SIZE = 32

    def __init__(self):
        self.table = [None] * HashTable.TABLE_SIZE

    def fnHash(self, key):
        """Returns a hash through a simple hashing function"""
        hash = 0
        for letter in key:
            # The letters' ASCII values are added up
            hash += ord(letter)

        return hash % HashTable.TABLE_SIZE

    def insert(self, key, value):
        """Inserts a key and value in the table"""
        index = self.fnHash(key)

        # If there is no linked list at the index, create one
        if self.table[index] == None:
            self.table[index] = LinkedList()
            
        self.table[index].insert((key, value))

    def remove(self, key):
        """Removes a value from the hash table"""
        index = self.fnHash(key)
        linkedList = self.table[index]

        if linkedList != None:
            # If the item is present, remove it
            if linkedList.find(key) != None:
                current = linkedList.head

                while current != None:
                    if current.data[0] == key:
                        linkedList.remove(current.data)
                        return

                    current = current.next
            else:
                print("Your item does not exist")
    
    def __str__(self):
        """Returns a string representation of the mutant hash table to visualize it"""
        sList = ""
        for i in range(HashTable.TABLE_SIZE):
            # Ternary operator -> empty linked lists are left out
            sList += "{} ==> {}\n".format(i, self.table[i]) if self.table[i] != None else ""

        return sList

    def merge(self, other):
        """Merge two hash tables"""
        merged = HashTable()

        for i in range(HashTable.TABLE_SIZE):
            # You can not call a function from None
            if self.table[i] is None:
                if other.table[i] is None:
                    continue

                # If the other hash table is not None, just add it to the new hash table
                # The reason I am copying them is if I change the new hash table, the original hash won't be affected
                merged.table[i] = other.table[i].copy()
            else:
                if other.table[i] is None:
                    merged.table[i] = self.table[i].copy()
                    continue

                merged.table[i] = self.table[i].merge(other.table[i])

        return merged

    def count(self):
        """Returns the number of elements inside the hash table"""
        length = 0

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            length += self.table[i].count()

        return length

    def getList(self):
        """Returns the lists with more than one key in a LIST"""
        lists = []
        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue
            
            if self.table[i].count() > 1:
                lists.append(self.table[i])
            
        return lists

    def find(self, key):
        """Returns the value of based on the key"""
        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue
            
            if self.table[i].find(key) is None:
                continue
            else:
                return self.table[i].find(key)

        print("Your item is not in the list")

    
    #### Transforming into other data structures ####

    def toStack(self, val="values"):
        stack = Stack()
        if val == "values":
            index = 1
        elif val == "keys":
            index = 0
        else:
            print("The only accepted arguments are 'keys' and 'values'")
            return

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            current = self.table[i].head

            while current is not None:
                stack.push(current.data[index])
                current = current.next
            
        return stack

    def toQueue(self, val="values"):
        queue = Queue()
        if val == "values":
            index = 1
        elif val == "keys":
            index = 0
        else:
            print("The only accepted arguments are 'keys' and 'values'")
            return

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            current = self.table[i].head

            while current is not None:
                queue.enqueue(current.data[index])
                current = current.next
            
        return queue
    
    def toBST(self):
        binTree = BST()
        hasDataType = False

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            current = self.table[i].head
            if not hasDataType:
                binTree.dataType = type(current.data[1])
                hasDataType = True

            while current is not None:
                if not isinstance(current.data[1], binTree.dataType):
                    print("Not all of the values are of the same data type.")
                    return

                binTree.insert(current.data[1])

                current = current.next

        return binTree