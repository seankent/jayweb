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

    ##########
    # gennav #
    ##########
    def gennav(self, name, depth = 0):
        """
        """
        params = {}

        params["id"] = name + "-" + "-".join(self.getpath())
        params["depth"] = str(depth)
        params["data-page-id"] = "-".join(self.getpath())

        params["nav-button"] = {}
        params["nav-button"]["text"] = self.value["title"]
        params["nav-button"]["href"] = "/".join(self.getpath()) + "/index.html"
        params["nav-button"]["depth"] = str(depth)

        if self.children != []:
            params["nav-button"]["toggle"] = "yes"
        else:
            params["nav-button"]["toggle"] = "no"

        #params["nav-button"]["indent"] = str(2*depth) 
        params["items"] = {} 

        for child in self.children:
            params["items"][child.name] = child.gennav(name, depth = depth + 1)

        return params

    #######
    # gen #
    #######
    def gen(self):
        """
        """
        params = {}

        params["head"] = {}
        params["body"] = {}
        params["body"]["header"] = {}
        params["body"]["nav"] = {}
        params["body"]["side-nav"] = {}
        params["body"]["main"] = {}
        params["body"]["footer"] = {}

        params["head"]["title"] = self.value["title"] 
        params["head"]["logo"] = ROOT + "/docs/diag/logo.svg" 
        params["head"]["base"] = ROOT + "/gen/index.html" 

        params["body"]["data-page-id"] = "-".join(self.getpath())

        params["body"]["header"]["nav-logo"] = {}
        params["body"]["header"]["nav-logo"]["src"] = ROOT + f"/docs/diag/bluejay_devices.svg"  
        params["body"]["header"]["nav-logo"]["alt"] = "logo" 

        params["body"]["header"]["navbar"] = {}

        
        params["body"]["header"]["navbar"]["items"] = {}
        params["body"]["header"]["navbar"]["items"]["about"] = {"href": ROOT + f"/gen/about/index.html", "text": "About"}
        params["body"]["header"]["navbar"]["items"]["contact"] = {"href": ROOT + f"/gen/contact/index.html", "text": "Contact"}
        params["body"]["header"]["navbar"]["items"]["docs"] = {"href": ROOT + f"/gen/products/index.html", "text": "Products"}



        params["body"]["nav"]["nav-item"] = self.root().gennav("nav")

        params["body"]["side-nav"]["nav-item"] = self.root().gennav("side-nav")


        if self.name[:4] == "test":
            params["body"]["main"]["src"] = ROOT + f"/docs/index.py" 
        else:
            params["body"]["main"]["src"] = ROOT + f"/docs/{self.name}.py" 
        params["body"]["main"]["params"] = {} 



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

    for i in range(15):
        root.get(["products", "jay40"]).add(Jaypage(f"test{i}", {
            #"title": "DemoXXXXXXXXXXXXXXXXXXXXX Click Me!! Please",
            "title": f"Test {i}",
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
    params = page.gennav("nav")
    print(params)
    print(page.gen())

    txt = jayweb.include(f"{ROOT}/include/html.py", params = page.gen())
    #page.build()
    page.buildall()
    #jayweb.write(f'{ROOT}/gen/index.html', txt)



    
