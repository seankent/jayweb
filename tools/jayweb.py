import textwrap

###########
# Jayweb #
###########
class Jayweb:
    ############
    # __init__ #
    ############
    def __init__(self):
        """
        """
        pass

    ########
    # read #
    ########
    def read(self, filename):
        """
        Reads from the specified file. 
        
        Arguments:
            filename (str): Name of file.
        """
        with open(filename, 'r') as file:
            return file.read()

    #########
    # write #
    #########
    def write(self, filename, txt):
        """
        Writes txt to the specified file. 
        
        Arguments:
            filename (str): Name of file.
            txt (str): String of text to be written.
        """
        with open(filename, 'w') as file:
            file.write(txt)
        
    ##########
    # indent #
    ##########
    def indent(self, txt, n = 0):
        """
        """
        return textwrap.indent(txt, " "*n)

    ###########
    # include #
    ###########
    def include(self, filename, params = None):
        """
        """
        if params is None:
            params = {}

        namespace = {"jayweb": self, "params": params}

        exec(self.read(filename), namespace)
      
        return namespace["txt"] 

    ############
    # includef #
    ############
    def includef(self, filename, params = None, n = 0):
        """
        """
        return self.indent(self.include(filename, params), n)

    ##############
    # preprocess #
    ##############
    def preprocess(self, config):
        """
        """
        pass

    #########
    # mount #
    #########
    def mount(self, config):
        """
        """
        if "children" in config:
            for child in config["children"]:
                if config["children"][child]["type"] == "mount":
                    config["children"][child] = self.load(filename = config["children"][child]["filename"], params = config["children"][child]["params"])["config"]
                
                self.mount(config["children"][child])

    #######
    # gen #
    #######
    def gen(self, config):
        """
        """
        txt = f""

        if config["type"] == "text":
            txt += config["text"]     

        else:
            txt += f"<{config['type']}"
            for attr, value in config["attr"].items():
                txt += f" {attr}=\"{value}\""
            txt += f">\n"
            
            for child in sorted(config["children"], key=lambda x: float(config["order"][x])):
                txt += self.indent(self.gen(config["children"][child])) 
                txt += "\n" 

            txt += f"</{config['type']}>"

        return txt
        



if __name__ == '__main__':
    
    config = {
        "type": "div",
        "attr": {"class": "class-0"},
        "order": {"c1": "1", "c2": "0"},
        "children": {},
    }


    config["children"]["c1"] = {
        "type": "none",
        "text": "Hello World",
    }

    config["children"]["c2"] = {
        "type": "none",
        "text": "Hello There",
    }

    config["children"]["c2"] = {
        "type": "div",
        "attr": {"class": "class-1"},
        "order": {},
        "children": {},
    }

    #config["children"]["c2"]["children"]["c2c1"] = {
    #    "type": "div",
    #    "params": {"class": "header-item"},
    #    "order": "0",
    #    "children": {},
    #}

    txt = "" 
    txt += "<div>\n" 
    txt += "</div>\n" 

    params = {"title": "Jayweb | Home"}

    jayweb = Jayweb()
    txt = jayweb.include("./include/main.py", params = params)
    print(txt)

    #config = jayweb.load("./include/boilerplate.py")["config"]

    #jayweb.mount(config)

    #print(config)
    #print(jayweb.gen(config))
    jayweb.write("./index.html", txt)

    
