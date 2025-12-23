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
#txt += f'    <base href="{params["base"]}">\n'
txt += f'    <link rel="icon" href="{params["favicon"]}">\n'
txt += f'    <link rel="stylesheet" href="/css/styles.css">\n'
txt += f'    <link rel="stylesheet" href="/css/content.css">\n'
txt += f'    <link rel="stylesheet" href="/css/syntax.css">\n'
txt += f'<link rel="preconnect" href="https://fonts.googleapis.com">'
txt += f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
txt += f'<link href="https://fonts.googleapis.com/css2?family=Averia+Libre:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap" rel="stylesheet">'

#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/styles.css">\n'
#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/content.css">\n'
#txt += f'    <link rel="stylesheet" href="{params["ROOT"]}/include/syntax.css">\n'
#txt += f'    <link href="https://cdn.jsdelivr.net/npm/overlayscrollbars/styles/overlayscrollbars.min.css" rel="stylesheet"/>\n'
#txt += f'    <script src="https://cdn.jsdelivr.net/npm/overlayscrollbars@2/browser/overlayscrollbars.browser.es5.min.js"></script>'
#txt += f'    <script\n'
#txt += f'      src="https://cdn.jsdelivr.net/npm/overlayscrollbars/browser/overlayscrollbars.browser.es6.min.js"\n'
#txt += f'      defer\n'
#txt += f'    ></script>\n'
txt += f'</head>\n'


