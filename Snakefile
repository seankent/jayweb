JAYWEB = "/Users/seankent/Documents/jayweb"

rule build:
    input:
        #jayweb = f"{JAYWEB}/tools/jayweb.py"
        jaypage = f"{JAYWEB}/tools/jaypage.py"
    shell:
        """
        python3 {input.jaypage}
        """
