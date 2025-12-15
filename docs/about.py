
txt = ''
#txt += f'<div class="content">\n'
#txt += jayweb.includemdf(f'{params["ROOT"]}/docs/about.md')
#txt += f'</div>\n'

#txt += jayweb.includemdf(f'{params["ROOT"]}/include/product-gallery.py')
txt += jayweb.includef(f'{params["ROOT"]}/include/product-gallery.py', {}, 4)
