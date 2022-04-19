class ChainingHashTable:
    # Constructor
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table
    # Returns the item if found
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # Removes an item with matching key from the hash table
    def remove(self, key):
        # get the bucket list where the item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])