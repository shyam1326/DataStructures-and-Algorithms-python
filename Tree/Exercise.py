


class TreeNode:
    def __init__(self,name, designation=None):
        self.name= name
        self.designation= designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent= self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent

        while parent:
            level +=1
            parent = parent.parent
        
        return level

    def print_tree(self, type= None, level=None):

        spaces = ' ' * self.get_level()*3
        prefix = spaces + '|__' if self.parent else ''
        try:
            if type == 'name':
                print(prefix + self.name)

                for child in self.children:
                    child.print_tree(type=type)

            elif type == 'designation':

                print(prefix + self.designation)

                for child in self.children:
                    child.print_tree(type=type)
            
            elif type == 'both':
                print(prefix + self.name + '('+ self.designation+')')

                for child in self.children:
                    child.print_tree(type=type)
        except Exception as e:
            raise e
        
        if level != None:
            if self.get_level() > level:
                return 
                
            print(prefix + self.name)

            for child in self.children:
                child.print_tree(level=level)
        





if __name__=="__main__":

# 1.Below is the management hierarchy of a company.
# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.

    # def build_hierarchy_tree():
    #     root = TreeNode("Nilpul", "CEO")

    #     CTO = TreeNode("Chinmay", "CTO")

    #     Infra = TreeNode('Vishwa', 'Infrastructure Head')
    #     Infra.add_child(TreeNode('Dhaval', 'Cloud manager'))
    #     Infra.add_child(TreeNode('Abijit','App Manager'))

    #     Application = TreeNode('Aamir', 'Application Head')
        
    #     HR = TreeNode('Gels', 'HR Head')
    #     HR.add_child(TreeNode('Peter', 'Recruitment manager'))
    #     HR.add_child(TreeNode('waqas', 'Policy manager'))

    #     root.add_child(CTO)
    #     root.add_child(HR)
    #     CTO.add_child(Infra)
    #     CTO.add_child(Application)
        
    #     return root

    # tree = build_hierarchy_tree()
    # tree.print_tree(type="name")
    # tree.print_tree(type="designation")
    # tree.print_tree(type="both")



# Now modify print_tree method to take tree level as input. And that should print tree only upto that level.

    def build_level_tree():

        root = TreeNode("Global")

        india = TreeNode("India")
        usa = TreeNode("USA")

        gujrat = TreeNode("Gujarath")
        gujrat.add_child(TreeNode("Ahamedabad"))
        gujrat.add_child(TreeNode("Baroda"))

        karnataka = TreeNode("Karnataka")
        karnataka.add_child(TreeNode("Bangalore"))
        karnataka.add_child(TreeNode("Mysore"))

        new_jersey = TreeNode("New Jersey")
        new_jersey.add_child(TreeNode("Princeton"))
        new_jersey.add_child(TreeNode("Trenton"))

        california = TreeNode("California")
        california.add_child(TreeNode("San Franciso"))
        california.add_child(TreeNode("Mountain view"))
        california.add_child(TreeNode("Palo Alto"))


        root.add_child(india)
        root.add_child(usa)

        india.add_child(gujrat)
        india.add_child(karnataka)

        usa.add_child(new_jersey)
        usa.add_child(california)

        
        return root

    tree = build_level_tree()
    tree.print_tree(level=0)
    tree.print_tree(level=1)
    tree.print_tree(level=2)
    tree.print_tree(level=3)