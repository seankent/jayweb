txt = ''

txt += f'<div class="side-nav" id="{params["side-nav-group"]}">\n'

for i in range(len(params["items"])):
    txt += jayweb.includef(f'{params["ROOT"]}/include/nav-item.py', params["items"][i], 4)

#for i in range(len(params["items"])):
#    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-item.py', params["items"][i], 4)

txt += f'</div>\n'
