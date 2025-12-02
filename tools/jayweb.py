import re
import textwrap
import markdown
from bs4 import BeautifulSoup

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
        print(repr(txt))
        return markdown.markdown(txt, extensions=['tables', 'fenced_code', 'codehilite', 'attr_list', "md_in_html"], extension_configs = {'codehilite': {'stripnl': True}})

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

    ###############
    # postprocess #
    ###############
    def postprocess(self, txt):
        """
        """
        while True:
            # check for a codehilite div block with one or more leading spaces
            match = re.search(r'^\s+<div\s+class=["\']codehilite["\'][^>]*>.*?</div>', txt, re.DOTALL | re.MULTILINE)


            if match is None:
                break

            print(match.group())

            txt = txt[:match.start()] + textwrap.dedent(match.group()) + txt[match.end():]
                





        ##pattern = r'<div\s+class=["\']codehilite["\'][^>]*>.*?</div>'
        #pattern = r'^\s*<div\s+class=["\']codehilite["\'][^>]*>.*?</div>'
        #matches = re.findall(pattern, txt, re.DOTALL | re.MULTILINE)
        #for match in matches:
        #    print("##########")
        #    print(match)

        ##for match in re.finditer(pattern, html, re.DOTALL):
        ##    print("Found match:")
        ##    print(repr(match.group()))
        ##    print(f"Start: {match.start()}, End: {match.end()}")

        #print("########################")
        #print("########################")
        #txt = """
        #    fun ():
        #        Hellow
        #        There
        #"""
        #txt = textwrap.dedent(txt)

        #print(txt)

        return txt


if __name__ == '__main__':
    jayweb = Jayweb()
    
    #txt = jayweb.read(f"{ROOT}/gen/about/index.html")
    txt = jayweb.includef(f"{ROOT}/include/box.py", {}, 0)
    txt = jayweb.postprocess(txt) 
    print(txt)
    jayweb.write(f"{ROOT}/gen/test.html", txt)

    
