

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

txt += f'<div class="main-left">\n'

if params["has-side-nav-menu"] == "yes":
    txt += jayweb.includef(f"{params['ROOT']}/include/side-nav-menu.py", params["side-nav-menu"], 4)

txt += f'</div>\n'




