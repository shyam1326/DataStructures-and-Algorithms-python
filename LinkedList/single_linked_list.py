# Create a Single LinkedList

class Node:
    def __init__(self,data, pointer):
        self.data = data
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_begining(self, data):
        self.head = Node(data, self.head)
        return
    
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        
        itr = self.head

        while itr.pointer:
            itr = itr.pointer
        
        itr.pointer = Node(data,  None)
        return
        
    def insert_list(self, data:list):
        for i in data:
            self.insert_end(i)
        return
    
    def get_length(self):

        itr = self.head
        count_head = 0

        while itr:
            count_head += 1
            itr = itr.pointer

        return count_head

    def insert_index(self,data,index):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index !!")
        if index ==0:
            self.insert_begining(data)
        
        itr = self.head
        itr_count = 0

        while itr:
            if itr_count == index-1:
                itr.pointer = Node(data, itr.pointer)

            itr = itr.pointer
            itr_count += 1
    
    def remove_first(self):

        itr = self.head

        while itr:
            self.head = itr.pointer
            break
        return

    def remove_last(self):

        itr = self.head
        itr_count = 0

        while itr:
            # print(self.get_length()-1)
            if itr_count == (self.get_length()-2):
                itr.pointer = None
                break

            itr = itr.pointer
            itr_count += 1
    def remove_index(self,index):
        if index <0 or index > self.get_length():
            raise Exception('Invalid Index')
            return
        if index == 0:
            self.head = self.head.pointer

        itr = self.head
        count_itr = 0

        while itr:
            if count_itr == index - 1:
                itr.pointer = itr.pointer.pointer

            itr = itr.pointer
            count_itr += 1

    def insert_after_value(self, search_value, insert_value):
        # if search_value not in self.head.data:
        #     raise Exception ('Value not found')
        
        itr = self.head
        count = 0

        while itr:
            if itr.data == search_value:
                self.insert_index(insert_value, count+1)
                return
            itr = itr.pointer
            count += 1
    
    def remove_by_value(self, search_value):
    # if search_value not in self.head.data:
    #     raise Exception ('Value not found')
    
        itr = self.head
        count = 0

        while itr:
            if itr.data == search_value:
                self.remove_index(count)
                return
            itr = itr.pointer
            count += 1 


    def print(self):

        itr = self.head
        string = ''
        while itr:
            string += str(itr.data) + '-->'
            itr = itr.pointer
        
        print(string)
    

if __name__=="__main__":
    obj = LinkedList()
    obj.insert_begining(5)
    obj.insert_begining(7)
    obj.insert_end(11)
    obj.insert_end(13)
    obj.insert_list(['a', 'b', 'c', 'd'])
    print(obj.get_length())
    obj.insert_index('sh',1)
    obj.remove_first()
    obj.remove_last()
    obj.remove_index(1)
    obj.insert_after_value('a', 'apple')
    obj.remove_by_value('a')
    obj.print()

