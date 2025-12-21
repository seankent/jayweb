
txt = ''

txt += f'<div class="board-overview">\n'
txt += f'    <div class="board-overview-text">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/markdown-content.py', {"src": f"{params['ROOT']}/pages/boards/jay40/jay40-header.md"}, 4)
txt += f'    </div>\n'
txt += f'    <div class="board-overview-image">\n'
txt += f'        <img src="diag/jay40.svg" alt="">\n'
txt += f'    </div>\n'
txt += f'</div>\n'
txt += f'<hr>\n'
