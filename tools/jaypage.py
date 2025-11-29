from treenode import TreeNode
from jayweb import Jayweb 
import re
import copy 
import os

ROOT = "/Users/seankent/Documents/jayweb"

jayweb = Jayweb()

###########
# Jaypage #
###########
class Jaypage(TreeNode):
    ############
    # __init__ #
    ############
    def __init__(self, name, value = None):
        """
        """
        super().__init__(name, value)

    ###########
    # __str__ #
    ###########
    def __str__(self):
        """
        """
        return f"Jaypage('{self.name}', {self.value})"

    ###########
    # gen_nav #
    ###########
    def gen_nav(self):
        """
        """
        params = {}
        params["text"] = self.value["title"]
        params["href"] = "/".join(self.getpath()) + "/index.html"
        params["id"] = "side-nav-item--root-" + "-".join(self.getpath())
        params["items"] = [] 

        for child in self.children:
            params["items"].append(child.gen_nav())

        return params

    #######
    # gen #
    #######
    def gen(self):
        """
        """
        params = {}

        params = {}
        params["head"] = {}
        params["body"] = {}
        params["body"]["header"] = {}
        params["body"]["header"]["nav"] = self.root().gen_nav()["items"]
        params["body"]["main"] = {}
        params["body"]["data-active-side-nav-item"] = "side-nav-item--root-" + "-".join(self.getpath())

        params["head"]["title"] = self.value["title"] 
        params["head"]["icon"] = ROOT + "/docs/diag/logo.svg" 
        params["head"]["base"] = ROOT + "/gen/index.html" 
        
        #params["body"]["main"]["md"] = ROOT + "/docs/about.py"
        params["body"]["main"]["md"] = ROOT + f"/docs/{self.name}.py"

        #if "side-nav" in self.value and self.value["side-nav"] == "self":
        #    params["body"]["main"]["side-nav"] = self.gen_nav()
        if "side-nav" in self.value:
            params["body"]["main"]["side-nav"] = self.root().get(self.value["side-nav"]).gen_nav()
            params["body"]["main"]["side-nav"]["side-nav-group"] = self.value["side-nav-group"] 
        else:
            params["body"]["main"]["side-nav"] = self.gen_nav()
            params["body"]["main"]["side-nav"]["side-nav-group"] = "none" 
            #params["body"]["main"]["side-nav"] = {"items": []} 


        return params

    #########
    # build #
    #########
    def build(self):
        """
        """
        txt = jayweb.include(f"{ROOT}/include/html.py", params = self.gen())
        print(txt)
        print(f"mkdir -p {ROOT}/gen/{"/".join(self.getpath())}")
        os.system(f"mkdir -p {ROOT}/gen/{"/".join(self.getpath())}")
        jayweb.write(f'{ROOT}/gen/{"/".join(self.getpath())}/index.html', txt)

    ############
    # buildall #
    ############
    def buildall(self):
        """
        """
        self.build()

        for child in self.children:
            child.buildall()




if __name__ == '__main__':
    

    root = Jaypage("index", {"title": "Home"})

    root.get([]).add(Jaypage("about", {
        "title": "About",
    }))

    root.get([]).add(Jaypage("contact", {
        "title": "Contact",
    }))

    root.get([]).add(Jaypage("products", {
        "title": "Products",
        "side-nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products"]).add(Jaypage("jay40", {
        #"title": "Jay40 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "title": "Jay40",
        "side-nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products", "jay40"]).add(Jaypage("configuration", {
        "title": "Configuration",
        "side-nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products", "jay40"]).add(Jaypage("demo", {
        #"title": "DemoXXXXXXXXXXXXXXXXXXXXX Click Me!! Please",
        "title": "Demo",
        "side-nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products"]).add(Jaypage("jaybtn", {
        "title": "JayBTN",
        "side-nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))


    page = root.get(["products", "jay40"])

    print(root)
    print(root.get(["about"]))
    print(root.get(["products", "jay40"]))
    
    page = root.get([])
    print(page.getpath())
    params = page.gen_nav()
    print(params)
    print(page.gen())

    txt = jayweb.include(f"{ROOT}/include/html.py", params = page.gen())
    #page.build()
    page.buildall()
    #jayweb.write(f'{ROOT}/gen/index.html', txt)



    
