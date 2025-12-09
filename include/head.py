if "title" not in params:
    params["title"] = ""

if "icon" not in params:
    params["icon"] = ""

if "base" not in params:
    params["base"] = "/"

txt = '' 


txt += f'<head>\n'
txt += f'    <meta charset="UTF-8">\n'
txt += f'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
txt += f'    <title>{params["title"]}</title>\n'
txt += f'    <link rel="icon" href="{params["icon"]}">\n'
#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/styles.css">\n'
#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/syntax.css">\n'
#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/content.css">\n'
#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/nav-styles.css">\n'
txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/new-styles.css">\n'
txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/new-nav-styles.css">\n'
txt += f'    <base href="{params["base"]}">\n'
txt += f'</head>\n'


