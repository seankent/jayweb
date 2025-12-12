

txt = ''

txt += f'<div class="nav-toggle-button">\n'
txt += f'    <a href="{params["href"]}">\n'
txt += f'        {params["text"]}\n'
txt += f'    </a>\n'
txt += f'    <div class="nav-button-chevron">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.5rem", "height": "1.5rem"}, 8)
txt += f'    </div>\n'
txt += f'</div>\n'

