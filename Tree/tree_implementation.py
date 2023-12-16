

class TreeNode:
    def __init__(self,data):
        self.data= data
        self.children= []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):

        level = 0
        print("printObject : ", self.parent)
        parent = self.parent
        while parent:
            level +=1
            parent = parent.parent
        
        return level
    
    def print_tree(self):

        spaces = ' ' * self.get_level()*3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)

        for child in self.children:
            child.print_tree()

if __name__=="__main__":

    def build_product_tree():
        root = TreeNode("Electronics")

        laptop = TreeNode('Laptop')
        laptop.add_child(TreeNode('Mac'))
        laptop.add_child(TreeNode('Surface'))
        laptop.add_child(TreeNode('ThinkPad'))

        cellphone = TreeNode('Cellphone')
        cellphone.add_child(TreeNode('Iphone'))
        cellphone.add_child(TreeNode('Google Pixel'))
        cellphone.add_child(TreeNode('One Plus'))

        tv = TreeNode('Tv')
        tv.add_child(TreeNode('Samsung'))
        tv.add_child(TreeNode('LG'))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(tv)

        return root

    tree = build_product_tree()
    tree.print_tree()