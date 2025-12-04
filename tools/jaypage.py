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
    def gen_nav(self, depth = 0):
        """
        """
        params = {}
        params["nav-button"] = {}
        params["nav-button"]["text"] = self.value["title"]
        params["nav-button"]["href"] = "/".join(self.getpath()) + "/index.html"
        params["nav-button"]["indent"] = str(max(1, 1*depth)) 

        params["nav-item-name"] = "nav-item-name--" + "-".join(self.getpath())
       
        if self.children != []:
            params["nav-button"]["toggle"] = "yes"
        else:
            params["nav-button"]["toggle"] = "no"

        #params["nav-button"]["indent"] = str(2*depth) 
        params["items"] = [] 

        for child in self.children:
            params["items"].append(child.gen_nav(depth = depth + 1))

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
        params["body"]["header"]["nav-logo"] = {"href": "#", "src": f'{ROOT}/docs/diag/bluejay_devices.svg'} 
        params["body"]["header"]["nav"] = self.root().gen_nav()
        params["body"]["header"]["nav"]["id"] = "main-nav" 
        params["body"]["main"] = {}
        params["body"]["nav-item-name"] = "nav-item-name--" + "-".join(self.getpath())

        if "nav-group" in self.value:
            params["body"]["nav-group"] = self.value["nav-group"]
        else:
            params["body"]["nav-group"] = "none" 

        params["head"]["title"] = self.value["title"] 
        params["head"]["icon"] = ROOT + "/docs/diag/logo.svg" 
        params["head"]["base"] = ROOT + "/gen/index.html" 
        
        #params["body"]["main"]["md"] = ROOT + "/docs/about.py"
        if "layout" in self.value:
            params["body"]["main"]["layout"] = self.value["layout"]
        else:
            params["body"]["main"]["layout"] = "default" 

        params["body"]["main"]["md"] = ROOT + f"/docs/{self.name}.py"

        #if "side-nav" in self.value and self.value["side-nav"] == "self":
        #    params["body"]["main"]["side-nav"] = self.gen_nav()
        if "side-nav" in self.value:
            params["body"]["main"]["side-nav"] = self.root().get(self.value["side-nav"]).gen_nav()
            params["body"]["main"]["side-nav"]["side-nav-group"] = self.value["nav-group"] 
        else:
            params["body"]["main"]["side-nav"] = self.gen_nav()
            params["body"]["main"]["side-nav"]["side-nav-group"] = "none" 


        params["body"]["main"]["side-nav"]["id"] = "side-nav" 

            #params["body"]["main"]["side-nav"] = {"items": []} 

        #params["body"]["main"]["side-nav"] = {"items": []} 


        return params

    #########
    # build #
    #########
    def build(self):
        """
        """
        txt = jayweb.postprocess(jayweb.include(f"{ROOT}/include/html.py", params = self.gen()))
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
        #"side-nav-group": "jay40-side-nav",
        #"side-nav": ["products"],
    }))

    root.get(["products"]).add(Jaypage("jay40", {
        #"title": "Jay40 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "title": "Jay40",
        "layout": "docs",
        "nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products", "jay40"]).add(Jaypage("configuration", {
        "title": "Configuration - This is a long Config section",
        "layout": "docs",
        "nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products", "jay40"]).add(Jaypage("demo", {
        #"title": "DemoXXXXXXXXXXXXXXXXXXXXX Click Me!! Please",
        "title": "Demo",
        "layout": "docs",
        "nav-group": "jay40-side-nav",
        "side-nav": ["products"],
    }))

    root.get(["products"]).add(Jaypage("jaybtn", {
        "title": "JayBTN",
        "layout": "docs",
        "nav-group": "jay40-side-nav",
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



    
