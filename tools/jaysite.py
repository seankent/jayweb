import re
import copy 
import textwrap
import markdown


###########
# Jaysite #
###########
class Jaysite:
    ############
    # __init__ #
    ############
    def __init__(self, config):
        """
        """
        self.config = copy.deepcopy(config)

    ###########
    # __str__ #
    ###########
    def __str__(self):
        """
        """
        return f"Jaysite({self.config})"

    ############
    # __repr__ #
    ############
    def __repr__(self):
        """
        """
        return self.__str__()

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
    # gennav #
    ##########
    def gennav(self, webpage):
        """
        """
        params = {}
        params["href"] = webpage



         




if __name__ == '__main__':
    

    config = {}
    
    config["webpages"] = {}

    config["webpages"]["index"] = {
        "title": "Home",
    }

    config["webpages"]["about"] = {
        "title": "About",
    }

    config["webpages"]["contact"] = {
        "title": "Contact",
    }

    config["webpages"]["products"] = {
        "title": "Products",
        "children": ["products/jay40", "products/jaybtn"],
    }

    config["webpages"]["products/jay40"] = {
        "title": "Jay40",
    }

    config["webpages"]["products/jaybtn"] = {
        "title": "JayBTN",
    }

    jaysite = Jaysite(config)
    print(jaysite)



    
