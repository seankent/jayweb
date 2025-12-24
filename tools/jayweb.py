import re
import textwrap
import markdown
from bs4 import BeautifulSoup
from pathlib import Path

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
        params["PWD"] = Path(filename).parent 

        namespace = {"jayweb": self, "params": params}

        self.exec(self.read(filename), namespace)
      
        return namespace["txt"] 

    ############
    # includef #
    ############
    def includef(self, filename, params = None, n = 0):
        """
        """
        #print(filename)
        #print(params)
        return self.indent(self.include(filename, params), n)

    ############
    # markdown #
    ############
    def markdown(self, txt):
        """
        """
        #return markdown.markdown(txt, extensions=['tables', 'fenced_code', 'codehilite', 'nl2br'])
        txt = markdown.markdown(txt, extensions=['tables', 'fenced_code', 'codehilite', 'attr_list', "md_in_html"], extension_configs = {'codehilite': {'stripnl': True, 'tab_length': 4}})

        # add table-wrapper around tables
        txt = re.sub(r'(<table>.*?</table>)', r'<div class="table-wrapper">\1</div>', txt, flags=re.DOTALL)

        # add img-wrapper around images 
        txt = re.sub(r'(<img.*?/>)', r'<div class="img-wrapper">\1</div>', txt, flags=re.DOTALL)

        return txt

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
        #i = 0
        #while True:


        #    # check for a codehilite div block with one or more leading spaces
        #    #match = re.search(r'^\s+<div\s+class=["\']codehilite["\'][^>]*>.*?</div>', txt, re.DOTALL | re.MULTILINE)


        #    #if match is None:
        #    #    break

        #    print(f"###################################################")
        #    print(f"##################### {i} #########################")
        #    print(f"###################################################")
        #    print(match.group())

        #    #txt = txt[:match.start()] + textwrap.dedent(match.group()) + txt[match.end():]


        #    soup = BeautifulSoup(txt, 'html.parser')

        #    
        #        

        #    i += 1

        #    if i == 3:
        #        break


        soup = BeautifulSoup(txt, 'html5lib')

        #for div in soup.find_all('div', class_='codehilite'):
        #    print(txt)

        #for div in soup.find_all('div', class_='codehilite'):
        #    print(f"###################################################")
        #    print(f"###################################################")

        #    #print(str(div)) 
        #    
        #    #print(re.sub(r'^\s+', '', str(div), flags=re.MULTILINE)) 


        #    #div.replace_with(BeautifulSoup(re.sub(r'^\s+', '', str(div), flags=re.MULTILINE), 'html.parser'))


        #    new_div = BeautifulSoup(re.sub(r'^\s+', '', str(div), flags=re.MULTILINE))

        #    div.replace_with(new_div)

        for div in soup.find_all('div', class_='codehilite'):
            content = div.decode_contents()
            dedented = re.sub(r'^ +', '', content, flags=re.MULTILINE)


            div.clear()
            div.append(BeautifulSoup(dedented, 'html5lib').find('pre'))

            wrapper = soup.new_tag('div', **{'class': 'code-wrapper'})

            div.wrap(wrapper)

        txt = str(soup)

        for div in soup.find_all('div', class_='codehilite'):
            print(txt)

        

            #print(textwrap.dedent(div.get_text()))

        # check for a codehilite div block with one or more leading spaces


        ## add table-wrapper around tables
        #txt = re.sub(r'(<table>.*?</table>)', r'<div class="table-wrapper">\1</div>', txt, flags=re.DOTALL)

        ## add img-wrapper around images 
        #txt = re.sub(r'(<img.*?/>)', r'<div class="img-wrapper">\1</div>', txt, flags=re.DOTALL)




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

    
