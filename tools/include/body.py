
txt = ''

txt += f'<body>\n'
txt += jayweb.includef(f'{params["ROOT"]}/tools/include/header.py', {}, 4) 
txt += jayweb.includef(f'{params["ROOT"]}/tools/include/main.py', {}, 4) 
txt += jayweb.includef(f'{params["ROOT"]}/tools/include/footer.py', {}, 4) 
txt += f'</body>\n'


