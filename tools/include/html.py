txt = '' 

txt += f'<!DOCTYPE html>\n'
txt += f'<html lang="en">\n'
txt += jayweb.includef("./include/head.py", {"title": params["title"]}, 4) 
txt += jayweb.includef("./include/body.py", {}, 4) 
txt += f'</html>\n'

