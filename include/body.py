
txt = ''
txt += f'<body data-page-id="{params["data-page-id"]}">\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 

#txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 

txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav.py', params["side-nav"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/footer.py', params["footer"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/footer.py', params["footer"], 4) 

#txt += f'<script src="https://cdn.jsdelivr.net/npm/overlayscrollbars@2/browser/overlayscrollbars.browser.es5.min.js"></script>\n'
txt += f'<script src="{params["ROOT"]}/include/app.js"></script>\n'
txt += f'</body>\n'


