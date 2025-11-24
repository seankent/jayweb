txt = '' 

txt += f'<!DOCTYPE html>\n'
txt += f'<html lang="en">\n'
txt += jayweb.includef(f'{params["ROOT"]}/tools/include/head.py', {"title": params["title"], "icon": params["icon"], "base": params["base"]}, 4) 
txt += jayweb.includef(f'{params["ROOT"]}/tools/include/body.py', {}, 4) 
txt += f'</html>\n'

