from collections import deque

class Stack:
    def __init__(self):
        self.element = deque()

    def push(self, val):
        return self.element.append(val)
    
    def pop(self):
        return self.element.pop()
    
    def peek(self):
        return self.element[-1]
    
    def is_empty(self):
        return len(self.element) == 0
    
    def size(self):
        return len(self.element)
    
    def reverse(self):
        rev = []
        for i in range(1, self.size()+1):
            rev.append(self.element[-i])
        
        print(rev)



if __name__=="__main__":
    obj = Stack()
    obj.push(5)
    obj.push(15)
    obj.push("We will conquere COVID-19")
    obj.push(25)
    obj.reverse()
    # obj.pop()
    # print(obj.peek())
    # print(obj.is_empty())
    # print(obj.size())
