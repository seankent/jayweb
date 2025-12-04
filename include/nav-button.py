if "href" not in params:
    params["href"] = "#" 

txt = ''
txt += f'<div class="nav-button">\n'

txt += f'    <a class="nav-button-text" href="{params["href"]}" style="padding-left: {params["indent"]}rem">\n'
txt += f'        {params["text"]}\n'
txt += f'    </a>\n'

if params["toggle"] == "yes":
    txt += f'    <div class="nav-button-chevron">\n'
    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35rem", "height": "1.35rem"}, 4)
    txt += f'    </div>\n'
else:
    txt += f'    <div>\n'
    txt += f'    </div>\n'

txt += f'</div>\n'

