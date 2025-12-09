
txt = ''

#txt += f'<body data-nav-item-name="{params["nav-item-name"]}" data-nav-group="{params["nav-group"]}">\n'
txt += f'<body data-nav-item-name="{params["nav-item-name"]}">\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/navbar.py', params["navbar"], 4) 

#txt += f'    <div class="temp-block-1">\n'
#txt += f'    </div>\n'
#
#txt += f'    <div class="temp-block-2">\n'
#txt += f'    </div>\n'

#txt += f'    <div class="temp-block-3">\n'
#txt += f'    </div>\n'

txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 

#txt += jayweb.includef(f'{params["ROOT"]}/include/footer.py', {}, 4) 
txt += f'<script src="{params["ROOT"]}/include/app.js"></script>\n'
txt += f'</body>\n'


