txt = '' 

txt += f'<!DOCTYPE html>\n'
txt += f'<html lang="en">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/head.py', params["head"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/body.py', params["body"], 4) 
txt += f'</html>\n'

