

txt = ''
txt += f'<div class="main">\n'
#txt += jayweb.includef(f"{params['ROOT']}/docs/demo.py", {}, 4)
txt += jayweb.includef(params["src"], params["params"], 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/footer.py', params["footer"], 4) 
txt += f'</div>\n'
