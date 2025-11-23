#<!DOCTYPE html>
#<html lang="en">
#
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width,
#                                   initial-scale=1.0">
#    <title>My Project</title>
#
#    <!-- To link external styling file -->
#    <link rel="stylesheet" href="styles.css">
#</head>
#
#<body>
#    <header>
#        <h1>
#            Welcome to My GeeksforGeeks
#        </h1>
#    </header>
#    <main>
#        <p>
#            This is where your content goes.
#        </p>
#    </main>
#    <footer>
#        <p>&copy; 2024 My Project</p>
#    </footer>
#    <!-- To link external javascript file -->
#    <script src="scripts.js"></script>
#</body>
#
#</html>



config = {
    "type": "html",
    "attr": {"lang": "en"},
    "order": {"head": "0", "body": "1"},
    "children": {"head": {}, "body": {}},
}

config["children"]["head"] = {
    "type": "head",
    #"attr": {"charset": "utf-8"},
    "attr": {},
    "order": {"meta": "0", "title": "1", "link": "2"},
    "children": {},
}

config["children"]["head"]["children"]["meta"] = {
    "type": "meta",
    "attr": {"charset": "utf-8", "name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    "order": {},
    "children": {},
}

config["children"]["head"]["children"]["title"] = {
    "type": "title",
    "attr": {},
    "order": {"title-text": "0"},
    "children": {},
}

config["children"]["head"]["children"]["title"]["children"]["title-text"] = {
    "type": "text",
    "text": "Jayweb | Home",
}

config["children"]["head"]["children"]["title"] = {
    "type": "link",
    "attr": {"rel": "stylesheet", "href": "./include/styles.css"},
    "order": {},
    "children": {},
}

config["children"]["body"] = {
    "type": "body",
    "attr": {},
    "order": {"mnt": "0"},
    "children": {},
}

config["children"]["body"]["children"]["mnt"] = {
    "type": "mount",
    "filename": "./include/header.py",
    "params": {"text": "Hell Yeah!"},
}
