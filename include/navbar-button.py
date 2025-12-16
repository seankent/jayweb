if "href" not in params:
    params["href"] = "#"

txt = ''
txt += f'<a href="{params["href"]}" class="button navbar-button">\n'
txt += f'    {params["text"]}\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-logo.py', params["nav-logo"], 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-toggle.py', {}, 4) 
txt += f'</a>\n'
