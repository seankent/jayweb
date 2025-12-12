

txt = ''
txt += f'<div class="sidebar-header">\n'
txt += f'    <img src="{params["ROOT"]}/docs/diag/bluejay_devices.svg" alt="">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 4) 
txt += f'</div>\n'
