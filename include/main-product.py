txt = ''
txt += f'<div class="main-product">\n'                                                                                                                                               
txt += f'    <div class="main-product-head">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/product-gallery.py', {}, 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/markdown-content.py', {"md": f'{params["ROOT"]}/docs/product-info.md'}, 4)
txt += f'    </div>\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/markdown-content.py', {"md": f'{params["ROOT"]}/docs/product-info-cont.md'}, 4)
txt += f'</div>\n'
