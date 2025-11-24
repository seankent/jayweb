JAYWEB = "/Users/seankent/Documents/jayweb"

rule build:
    input:
        jayweb = f"{JAYWEB}/tools/jayweb.py"
    shell:
        """
        python3 {input.jayweb}
        """
