


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if self.data == data:
            return
        #left child
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        #Right child
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)
    
    def search(self,val):
        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)

            else:
                return False
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False    
    def minimum(self):
        if self.left:
            return self.left.minimum()
        else:
            return self.data
    
    def maximum(self):
        if self.right:
            return self.right.maximum()
        else:
            return self.data

    def sum(self):
        left_res = 0
        if self.left:
            left_res += self.left.sum()

        right_res = 0
        if self.right:
            right_res += self.right.sum()
        
        return self.data + left_res + right_res
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.left
            
            elif self.right is None:
                return self.left
        
            max_val = self.left.maximum()
            self.data = min_val
            self.left = self.left.delete(max_val)
            
        return self
    
    def in_order_traversal(self):
        element = []

        # Visit left child
        if self.left:
            element += self.left.in_order_traversal()
        
        # Visit Base Node
        element.append(self.data)

        # Visit the right child
        if self.right:
            element += self.right.in_order_traversal()

        return element
    
    def pre_order_traversal(self):
        element = [self.data]

        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element
    
    def post_order_traversal(self):
        element = []

        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)

        return element

if __name__=="__main__":

    def build_tree(element):
        root = BinaryTreeNode(element[0])

        for i in range(1, len(element)):
            root.add_child(element[i])
        
        return root
    

    numbers = [17,4,1,20,9,23,18,34]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    print(tree.search(7))
    print(tree.search(4))
    print(tree.minimum())
    print(tree.maximum())
    print(tree.sum())
    print(tree.delete(20))
    print(tree.in_order_traversal())
    # print(tree.pre_order_traversal())
    # print(tree.post_order_traversal())

    # countries = ["India", "Pakistan", "USA", "UK", "Germany", "China"]
    # tree = build_tree(countries)
    # print(tree.in_order_traversal())
    # print("Uk is in the list : ", tree.search("UK"))
    # print("Sweden is in the list : ", tree.search("Sweden"))
