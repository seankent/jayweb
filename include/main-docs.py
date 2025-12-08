

txt = ''

#if params["layout"] == "docs":
#    txt += f'<div class="main-docs">\n'
#    #txt += jayweb.includef(f"{params['ROOT']}/include/side-nav.py", params["side-nav"], 4)
#    txt += jayweb.includef(f"{params['ROOT']}/include/nav.py", params["side-nav"], 4)
#    txt += jayweb.includef(f'{params["md"]}', {}, 4)
#    txt += f'</div>\n'
#
#else:
#    txt += f'<div class="main">\n'
#    txt += jayweb.includef(f'{params["md"]}', {}, 4)
#    txt += f'</div>\n'


#if params["layout"] == "docs":
#    txt += f'<div class="main main-side-nav">\n'
#else:

txt += f'<div class="main-docs">\n'
txt += jayweb.includef(f"{params['ROOT']}/include/side-nav-menu.py", params["side-nav-menu"], 4)

txt += f'    <div class="docs-content">\n'
txt += jayweb.includef(f"{params['ROOT']}/include/markdown-content.py", params["markdown-content"], 4)
txt += f'    </div>\n'
txt += f'</div>\n'




