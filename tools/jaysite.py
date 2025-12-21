from jaypage import Jaypage

########
# Home #
########
config = {}
config["title"] = "Home"
config["favicon"] = "/images/logo.svg"
config["logo"] = "/images/bluejay_devices.svg"
config["site"] = "Bluejay Devices"
config["footer-text"] = "&copy; 2025 Bluejay Devices"


root = Jaypage("index", config)


#########
# About #
#########
config = {}
config["title"] = "About"

root.get([]).add(Jaypage("about", config))

##########
# Boards #
##########
config = {}
config["title"] = "Boards"

root.get([]).add(Jaypage("boards", config))

#################
# Boards::Jay40 #
#################
config = {}
config["title"] = "Jay40"

root.get(["boards"]).add(Jaypage("jay40", config))



root.init()
root.buildall()


    
