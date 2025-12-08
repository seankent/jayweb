if "items" not in params:
    params["items"] = []

txt = ''

txt += f'<a class="button">\n'
txt += f'    {params["text"]}\n'

#for i in range(len(params["items"])):
#
#    if params["items"][i]["type"] == "text":
#        txt += f'    {params["items"][i]["text"]}\n'
#
#    if params["items"][i]["type"] == "icon":
#        txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35rem", "height": "1.35rem"}, 4)

txt += f'</a>\n'

