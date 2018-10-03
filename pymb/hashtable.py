from .sortedlinkedlist import SortedLinkedList
from .stack import Stack
from .queue import Queue
from .bst import BST

class HashTable:
    """Object that behaves like a hash table (almost! it is mutant >:O)
    
    * To insert a value, use hash[key] = value,
    * To get a value, use hash[key],
    * To delete a value, use del hash[key],
    * To use the hash function, use hash.fnHash(val) or pymb.hashtable.fnHash(val) (TODO: needs refactoring),
    * To transform into a bst, stack or queue, use hash.to"DATATYPE"(),
    * To merge two hash tables, use hash.merge(other),
    * To get the length of a hash table, use hash.count
    """
    TABLE_SIZE=32

    def __init__(self, dictionary=None):
        self.table=[None] * HashTable.TABLE_SIZE
        # If dictionary passed as an argument
        if isinstance(dictionary, dict):
            self.insert(dictionary)

    @classmethod
    def fnHash(cls, key):
        """Returns a hash through a simple hashing function"""
        hash=0
        for letter in key:
            # The letters' ASCII values are added up
            hash += ord(letter)

        return hash % HashTable.TABLE_SIZE

    def __setitem__(self, key, value):
        """Inserts a key and value in the table"""
        index=self.fnHash(key)

        # If there is no linked list at the index, create one
        if self.table[index] == None:
            self.table[index]=SortedLinkedList()

        self.table[index].insert((key, value))

    def __getitem__(self, key):
        index=self.fnHash(key)

        current = self.table[index].head
        while current is not None:
            if current.data[0] == key:
                return current.data[1]
            current = current.next

        raise ValueError("Item not found")
    
    def __delitem__(self, key):
        """Removes a value from the hash table"""
        index = self.fnHash(key)
        self.table[index].removeByKey(key)

    def insertDict(self, dictionary):
        """Inserts a dictionary to the hash table"""
        for key in dictionary:
            self[key] = dictionary[key]

    def __str__(self):
        """Returns a string representation of the mutant hash table to visualize it"""
        string=""
        for i in range(HashTable.TABLE_SIZE):
            # Ternary operator -> empty linked lists are left out
            string += "{} ==> {}\n".format(i,
                                          self.table[i]) if self.table[i] != None else ""

        return string[:-1]

    def merge(self, other):
        """Merge two hash tables"""
        merged=HashTable()

        for i in range(HashTable.TABLE_SIZE):
            # You can not call a function from None
            if self.table[i] is None:
                if other.table[i] is None:
                    continue

                # If the other hash table is not None, just add it to the new hash table
                # The reason I am copying them is if I change the new hash table, the original hash won't be affected
                merged.table[i]=other.table[i].copy()
            else:
                if other.table[i] is None:
                    merged.table[i]=self.table[i].copy()
                    continue

                merged.table[i]=self.table[i].merge(other.table[i], isHash=True)

        return merged

    @property
    def count(self):
        """Returns the number of elements inside the hash table"""
        length=0

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            length += self.table[i].count()

        return length

    #### Transforming into other data structures ####

    def toStack(self, val="values"):
        stack=Stack()
        if val == "values":
            index=1
        elif val == "keys":
            index=0
        else:
            print("The only accepted arguments are 'keys' and 'values'")
            return

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            current=self.table[i].head

            while current is not None:
                stack.push(current.data[index])
                current=current.next

        return stack

    def toQueue(self, val="values"):
        queue=Queue()
        if val == "values":
            index=1
        elif val == "keys":
            index=0
        else:
            print("The only accepted arguments are 'keys' and 'values'")
            return

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            current=self.table[i].head

            while current is not None:
                queue.enqueue(current.data[index])
                current=current.next

        return queue

    def toBST(self):
        binTree=BST()
        hasDataType=False

        for i in range(HashTable.TABLE_SIZE):
            if self.table[i] is None:
                continue

            current=self.table[i].head
            if not hasDataType:
                binTree.dataType=type(current.data[1])
                hasDataType=True

            while current is not None:
                if not isinstance(current.data[1], binTree.dataType):
                    print("Not all of the values are of the same data type.")
                    return

                binTree.insert(current.data[1])

                current=current.next

        return binTree
