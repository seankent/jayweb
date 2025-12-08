params["items"] = [{"src": f'{params["ROOT"]}/docs/diag/jay40.svg'}, {"src": f'{params["ROOT"]}/docs/diag/bluejay_devices.svg'}, {"src": f'{params["ROOT"]}/docs/diag/bluejay_devices_plain.svg'}, {"src": f'{params["ROOT"]}/docs/diag/logo.svg'}]

txt = ''
txt += f'<div class="product-gallery">\n'

txt += f'    <div class="product-gallery-image">\n'
txt += f'        <img src="{params["ROOT"]}/docs/diag/jay40.svg" alt="">\n'
txt += f'    </div>\n'

txt += f'    <div class="product-gallery-thumbnail-wrapper">\n'

for i in range(len(params["items"])):
    txt += f'           <div class="product-gallery-thumbnail">\n'
    txt += f'               <img src="{params["items"][i]["src"]}" alt="">\n'
    txt += f'           </div>\n'

txt += f'    </div>\n'
txt += f'</div>\n'
