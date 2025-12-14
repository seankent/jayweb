

txt = ''
txt += f'<div class="nav-button">\n'
txt += f'    <a href="{params["href"]}">\n'
txt += f'        {params["text"]}\n'
txt += f'    </a>\n'

if params["toggle"] == "yes":
    txt += f'    <div class="nav-button-chevron">\n'
    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "2rem", "height": "2rem"}, 8)
    txt += f'    </div>\n'
else:
    txt += f'    <a href="{params["href"]}">\n'
    txt += f'    </a>\n'


txt += f'</div>\n'

