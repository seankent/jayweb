import textwrap
import markdown

ROOT = "/Users/seankent/Documents/jayweb"

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

    ########
    # exec #
    ########
    def exec(self, txt, namespace = None):
        """
        """
        if namespace is None:
            namespace = {}

        exec(txt, namespace)
      
        return namespace

    ###########
    # include #
    ###########
    def include(self, filename, params = None):
        """
        """
        if params is None:
            params = {}

        params["ROOT"] = f"{ROOT}"

        namespace = {"jayweb": self, "params": params}

        self.exec(self.read(filename), namespace)
      
        return namespace["txt"] 

    ############
    # includef #
    ############
    def includef(self, filename, params = None, n = 0):
        """
        """
        print(filename)
        print(params)
        return self.indent(self.include(filename, params), n)

    ############
    # markdown #
    ############
    def markdown(self, txt):
        """
        """
        #return markdown.markdown(txt, extensions=['tables', 'fenced_code', 'codehilite', 'nl2br'])
        return markdown.markdown(txt, extensions=['tables', 'fenced_code', 'codehilite'], extension_configs = {'codehilite': {'stripnl': True}})

    #############
    # includemd #
    #############
    def includemd(self, filename):
        """
        """
        return self.markdown(self.read(filename))
        
    ##############
    # includemdf #
    ##############
    def includemdf(self, filename, n = 0):
        """
        """
        return self.indent(self.includemd(filename) + "\n", n)




if __name__ == '__main__':
    jayweb = Jayweb()
    

    #params = {"title": "Jayweb | Home", "icon": f"{ROOT}/docs/diag/logo.svg", "base": f"{ROOT}/gen/index.html"}
    params = jayweb.exec(jayweb.read(f'{ROOT}/site/jayconfig.py'), {"ROOT": ROOT})["params"]
    print(params)

    txt = jayweb.include(f"{ROOT}/include/html.py", params = params["html"])
    print(txt)

    jayweb.write(f'{ROOT}/gen/index.html', txt)
    #jayweb.write(f'{ROOT}/gen/jay40.html', txt)

    
