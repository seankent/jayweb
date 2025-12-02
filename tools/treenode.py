import re
import copy 
import textwrap
import markdown


############
# TreeNode #
############
class TreeNode:
    ############
    # __init__ #
    ############
    def __init__(self, name, value = None):
        """
        """
        self.name = name

        if value is None:
            self.value = {} 
        else:
            self.value = value
            
        self.parent = None
        self.children = [] 

    ###########
    # __str__ #
    ###########
    def __str__(self):
        """
        """
        return f"TreeNode('{self.name}', {self.value})"

    ############
    # __repr__ #
    ############
    def __repr__(self):
        """
        """
        return self.__str__()

    #######
    # add #
    #######
    def add(self, child):
        """
        """
        self.children.append(child)
        child.parent = self

    #######
    # get #
    #######
    def get(self, path):
        """
        """
        if path == []: 
            return self

        for child in self.children:
            if child.name == path[0]:
                return child.get(path[1:]) 

    ###########
    # getpath #
    ###########
    def getpath(self):
        """
        """
        if self.parent is None:
            return []
        else:
            return self.parent.getpath() + [self.name]


    ########
    # root #
    ########
    def root(self):
        """
        """
        if self.parent is None:
            return self
        else:
            return self.parent.root()

    #########
    # depth #
    #########
    def depth(self):
        """
        """
        if self.parent is None:
            return 0 
        else:
            return self.parent.depth() + 1



if __name__ == '__main__':
    

    index = TreeNode("index", {"title": "Home"})
    about = TreeNode("about", {"title": "About"})
    products = TreeNode("products", {"title": "Products"})
    jay40 = TreeNode("jay40", {"title": "Jay40"})
    jaybtn = TreeNode("jaybtn", {"title": "JayBTN"})

    index.add(about)
    index.add(products)
    products.add(jay40)
    products.add(jaybtn)

    #root.get(["products", "jay40"]).add({
    #    
    #})

    print(index)
    print(index.get([]))
    print(index.get(["products"]))
    print(index.get(["products", "jay40"]))
    #print(about)
    #print(about.root())
    #print(jay40)
    #print(jay40.root())


    
