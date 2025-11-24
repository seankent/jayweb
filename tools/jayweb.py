import textwrap
import markdown

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
    

    params = {"title": "Jayweb | Home", "icon": "./include/logo.svg"}

    jayweb = Jayweb()
    txt = jayweb.include("./include/html.py", params = params)
    print(txt)

    jayweb.write("./index.html", txt)

    
