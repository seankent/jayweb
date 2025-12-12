
txt = ''
txt += f'<body>\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/sidebar.py', params["sidebar"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 

txt += f'<script src="{params["ROOT"]}/include/app.js"></script>\n'
txt += f'</body>\n'


