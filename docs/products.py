
#txt = jayweb.includemdf(f'{params["ROOT"]}/docs/products.md')

txt = ''
txt += '<div class="product">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/gallery.py', {}, 4)
txt += '</div>\n'
