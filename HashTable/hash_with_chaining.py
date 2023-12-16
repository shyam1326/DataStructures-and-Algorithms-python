



class HashTable:
    def __init__(self):
        self.max = 10 # Size of a hashmap list/array
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.max   # To keep the hash value under the length of array

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]


if __name__=="__main__":
    obj = HashTable()
    obj['march 6'] = 20
    obj['march 6'] = 21
    obj['march 8'] = 25
    obj['march 17'] = 31
    obj['dec 6'] = 32

    print(obj.arr)
    print(obj['march 6'])
    print(obj['march 17'])
    del obj['march 17']
    print(obj['march 17'])
    print(obj.arr)



