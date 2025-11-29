if "href" not in params:
    params["href"] = "#" 
if "items" not in params:
    params["items"] = []
if "indent" not in params:
    params["indent"] = "0"


txt = ''

txt += f'<div class="nav-item">\n'

txt += f'    <a href="{params["href"]}" class="nav-button">\n'
#txt += f'        <div class="side-nav-button-label">\n'
txt += f'        <div class="">\n'
txt += f'            {"&nbsp;"*int(params["indent"]) + params["text"]}\n'
txt += f'        </div>\n'
txt += f'    </a>\n'

for i in range(len(params["items"])):
    params["items"][i]["indent"] = str(int(params["indent"]) + 2)
    txt += jayweb.includef(f'{params["ROOT"]}/include/nav-item.py', params["items"][i], 4)

txt += f'</div>\n'
