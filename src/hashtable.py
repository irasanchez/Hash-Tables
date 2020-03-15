# '''
# Linked List hash table key/value pair
# '''

# ORDER IS NOT GUARANTEED IN A HASH TABLE


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# HashTable: an array for storage and a hash function 👇
# the hash function will take a string and return a number
# the hash table uses the hash function to get an index in our storage array
# no longer need to iterate to lookup a value. We now just need the hash to find the index.

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    # _ means you cannot use this function outside of HashTable
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.

        % is the remainder after division has taken place
        hash % the total capacity makes sure we don't have indeces that are not included in the array's length 
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # use the has mod to turn our key into a hash
        index = self._hash_mod(key)

        # check in storage if something is at that index already.
        if self.storage[index] is not None:
            print(
                "this is where you will have the linked list add the new item to the tail")
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        self.storage[index] = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        return self.storage[hashed_key]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # for index in range(len(self.storage)):
        #     new_storage[index] = old_storage[index]


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
