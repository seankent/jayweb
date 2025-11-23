if "title" not in params:
    params["title"] = ""

txt = '' 

txt += f'<!DOCTYPE html>\n'
txt += f'<html lang="en">\n'

txt += f'<head>\n'
txt += f'    <meta charset="UTF-8">\n'
txt += f'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
txt += f'    <title>{params["title"]}</title>\n'
txt += f'    <link rel="stylesheet" href="./include/styles.css">\n'
txt += f'    <link rel="stylesheet" href="./include/syntax.css">\n'
txt += f'    <link rel="stylesheet" href="./include/content.css">\n'
txt += f'</head>\n'

txt += f'<body>\n'

txt += jayweb.includef("./include/header.py", {}, 4) 

txt += jayweb.includef("./include/main.py", {}, 4) 

txt += f'</body>\n'

txt += f'</html>\n'

