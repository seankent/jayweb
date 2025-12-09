if "max-width" not in params:
    params["max-width"] = "50rem"

txt = ''
txt += f'<div class="markdown-content" style="max-width: {params["max-width"]};">\n'
txt += jayweb.includemdf(params["md"], 4)
txt += f'</div>\n'




