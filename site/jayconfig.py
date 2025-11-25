
params = {}

params["html"] = {}

params["html"]["head"] = {
    "title": "Jayweb | Home",
    "icon": "/docs/diag/logo.svg",
    "base": f"{ROOT}/gen/index.html",
}

params["html"]["body"] = {}


params["html"]["body"]["header"] = {
    "nav": [
        {
            "type": "nav-button", 
            "href": "About",
            "text": "About"
        },
        {
            "type": "nav-button",
            "href": "Products",
            "text": "Products"
        },
        {
            "type": "nav-dropdown",
            "href": "#",
            "text": "Products",
            "items": [
                {
                    "href": "jay40.html",
                    "text": "Jay40",
                }, 
                {
                    "href": "#",
                    "text": "Chessa",
                },
                {
                    "href": "#",
                    "text": "Bradley R. Kent"
                },
                {
                    "href": "#",
                    "text": "Melissa R. Kent"
                },
            ]
        },
    ], 
}

params["html"]["body"]["main"] = {
    "md": f"{ROOT}/docs/about.md",
    #"md": f"{ROOT}/docs/jay40.md",
}


#params["html"]["body"]["header"]["nav"][1] = {
#    "type": "nav-button",
#    "href": "/Products",
#    "text": "Products",
#}
#
#params["html"]["body"]["header"]["nav"][3] = {
#    "type": "nav-dropdown",
#    "href": "#",
#    "text": "Contact",
#    "items": [
#        {"href": "#", "text": "Sean"},
#        {"href": "#", "text": "Chessa"},
#    ],
#}

#params["html"]["sub"]["body"]["sub"]["header"]["sub"]["contact"]["sub"]["sean"] = {
#    "href": "#",
#    "text": "Sean Kent",
#}
#
#params["html"]["sub"]["body"]["sub"]["header"]["sub"]["contact"]["sub"]["chessa"] = {
#    "href": "#",
#    "text": "Sean Kent",
#}



