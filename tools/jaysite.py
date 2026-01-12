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

###############################
# Boards::Jay40::Input/Output #
###############################
config = {}
config["title"] = "Input/Output"

root.get(["boards", "jay40"]).add(Jaypage("input_output", config))

################################
# Boards::Jay40::Configuration #
################################
config = {}
config["title"] = "Configuration"

root.get(["boards", "jay40"]).add(Jaypage("configuration", config))

########################
# Boards::Jay40::Power #
########################
config = {}
config["title"] = "Power"

root.get(["boards", "jay40"]).add(Jaypage("power", config))

##############################
# Boards::Jay40::Using a PLL #
##############################
config = {}
config["title"] = "Using a PLL"

root.get(["boards", "jay40"]).add(Jaypage("using_a_pll", config))

###################
# Boards::Bluejay #
###################
config = {}
config["title"] = "Bluejay"

root.get(["boards"]).add(Jaypage("bluejay", config))

###################################
# Boards::Bluejay::Board Overview #
###################################
config = {}
config["title"] = "Board Overview"

root.get(["boards", "bluejay"]).add(Jaypage("board_overview", config))



root.init()
root.buildall()


    
