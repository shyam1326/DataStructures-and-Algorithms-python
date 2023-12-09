# Create a double linked list

class Node:
    def __init__(self, data, pointer, prev_pointer=None):
        self.data = data
        self.pointer = pointer
        self.prev_pointer = prev_pointer

class DoubleLinkedList:
    def __init__(self):
        self.head =None
    
    def insert_begining(self, data):
        if self.head == None:
            self.head =  Node(data, self.head, None)

        else:
            node =  Node(data, self.head, None)
            self.head.prev_pointer = node
            self.head = node
        return
    
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,self.head, self.prev_pointer)
            return
        
        itr = self.head

        while itr.pointer:
            itr = itr.pointer
        
        itr.pointer = Node(data, None, itr.prev_pointer)
        return
    
    def get_last_node(self):
        itr = self.head

        while itr.pointer:
            itr = itr.pointer
        
        return itr
    
    def print_backward(self):

        last_node = self.get_last_node()
        itr = last_node
        string = ''
        while itr:
            string += str(itr.data) + '-->'
            itr = itr.prev_pointer

        print(string)


    
    def print_forward(self):

        itr = self.head
        string = ''
        while itr:
            string += str(itr.data) + '-->'

            itr = itr.pointer
        print(string)
    

if __name__=="__main__":
    obj = DoubleLinkedList()
    obj.insert_begining(5)
    obj.insert_begining(7)
    obj.insert_begining(11)
    # obj.insert_end(13)
    obj.print_forward()
    obj.print_backward()