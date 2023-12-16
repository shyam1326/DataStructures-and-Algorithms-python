

class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    
    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max
    
    def __setitem__(self,key, val):
        h = self.get_hash(key)
        counter = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key,value)
                counter = True
                break
            if not counter:
                self.arr[h].append((key,val))
            