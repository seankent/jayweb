if "href" not in params:
    params["href"] = "#" 

txt = ''
txt += f'<div class="nav-button">\n'
txt += f'    <a class="nav-button-text" href="{params["href"]}">\n'
txt += f'        {params["text"]}\n'
txt += f'    </a>\n'
txt += f'</div>\n'

