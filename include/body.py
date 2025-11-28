
txt = ''

txt += f'<body data-active-side-nav-item="{params["data-active-side-nav-item"]}">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/footer.py', {}, 4) 
txt += f'<script src="{params["ROOT"]}/include/app.js"></script>\n'
txt += f'</body>\n'


