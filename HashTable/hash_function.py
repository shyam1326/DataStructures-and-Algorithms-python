

class HashTable:
    def __init__(self):
        self.max = 100 # Size of a hashmap list/array
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char) # ord use the ascii number
        
        return h % self.max   # To keep the hash value under the length of array

    def __setitem__(self, key, val): # __setitem__ is a python component to access a ddictionary with index
        key = self.get_hash(key)
        self.arr[key] = val
    
    def __getitem__(self, key): # __getitem__ is a python component to access a ddictionary with index
        key = self.get_hash(key)
        return self.arr[key]
    
    def __delitem__(self, key):
        key = self.get_hash(key)
        self.arr[key] = None


if __name__=="__main__":
    obj = HashTable()
    obj['march 6'] = 20
    obj['march 8'] = 25
    obj['dec 6'] = 32

    print(obj['march 6'])
    del obj['march 6']
    print(obj['march 6'])



