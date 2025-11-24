
txt = ''

txt += f'<body>\n'
txt += jayweb.includef("./include/header.py", {}, 4) 
txt += jayweb.includef("./include/main.py", {}, 4) 
txt += jayweb.includef("./include/footer.py", {}, 4) 
txt += f'</body>\n'


