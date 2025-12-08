
//const sideNavButtons = document.querySelectorAll('.side-nav-button');

function toggleExpanded() {
    this.parentElement.parentElement.classList.toggle('nav-item-expanded');
    //console.log("toggleExpanded.");
}

function addNavExpanded() {
    this.parentElement.classList.add('navbar-expanded');
    //console.log("toggleExpanded.");
}

function removeNavExpanded() {
    this.parentElement.parentElement.classList.remove('navbar-expanded');
    //console.log("toggleExpanded.");
}

function setDisplayImage() {
    const item = document.querySelector('.product-gallery-image img');
    //item.classList.add('active');
    item.src = this.querySelector('img').src;
    //console.log("toggleExpanded.");
}

//function clearAllActive() {
//    this.parentElement.classList.toggle('active');
//    for (let sideNavItem of document.querySelectorAll('.side-nav-item')) {
//        sideNavItem.classList.remove('active');
//    }
//    console.log("setActive");
//}

//function setActive() {
//    for (let sideNavButton of document.querySelectorAll('.side-nav-button')) {
//        sideNavButton.classList.remove('active');
//    }
//    this.parentElement.classList.add('active');
//    console.log("setActive");
//}

function navButtonClick() {
    store();
    let config = JSON.parse(localStorage.getItem('config') || '{}');
    console.log(config);
    //debugger;
}

function setActive() {
    console.log("New Page");

    const currentPath = window.location.pathname;

    for (let link of document.querySelectorAll('.side-nav-button-text')) {
        if (currentPath.endsWith(link.getAttribute('href'))) {
            //link.classList.add('active');
            console.log("TRUE!!!");
            link.classList.add('active');
        }
    }
    //console.log(window.location.pathname);

    const sideNav = document.querySelector('.side-nav');

    let config = {};

    config["nav"] = "Sean";
    localStorage.setItem('config', JSON.stringify(config));
    
    console.log(sideNav.id);
    console.log(config["nav"]);

    config = JSON.parse(localStorage.getItem('config'));
    console.log(config);


}

function store()
{
    console.log("[INFO] Running 'store()'");

    let config = JSON.parse(localStorage.getItem('config') || '{}');

    if (!("nav" in config))
    {
        config["nav"] = {};
    }

    //if (document.querySelector('.nav'))
    //{
    //    config["nav"]["nav-group"] = document.body.getAttribute('data-nav-group');
    //}
    //else
    //{
    //    config["nav"]["nav-group"] = "none";
    //}

    //if (!("state" in config["nav"]))
    //{
    //    config["nav"]["state"] = {};
    //}

    for (let item of document.querySelectorAll(".nav-item"))
    {
        if (!(item.getAttribute('data-nav-item-name') in config["nav"]["state"]))
        {
            config["nav"]["state"][item.getAttribute('data-nav-item-name')] = {};
        }

        if (item.classList.contains("nav-item-expanded"))
        {
            console.log(item.getAttribute('data-nav-item-name'))
            config["nav"]["state"][item.getAttribute('data-nav-item-name')]["expanded"] = "yes";
        }
        else
        {
            config["nav"]["state"][item.getAttribute('data-nav-item-name')]["expanded"] = "no";
        }
    }


    console.log(config)
    //debugger;
    localStorage.setItem('config', JSON.stringify(config));
}

function load()
{
    console.log("[INFO] Running 'load()'");

    let config = JSON.parse(localStorage.getItem('config') || '{}');

    console.log(config);


    //if ("nav" in config && "nav-group" in config["nav"])
    //{
    //    
    //    if (document.querySelector('.nav'))
    //    {
    //        if (config["nav"]["nav-group"] !== document.body.getAttribute('data-nav-group'))
    //        {
    //            config["nav"]["state"] = {};
    //        }

    //    }
    //    else
    //    {
    //        config["nav"]["state"] = {};
    //    }
    //    if (config["nav"]["nav-group"] === "none") 
    //    {
    //        config["nav"]["state"] = {};
    //    }
    //}

    if ("nav" in config && "nav-group" in config["nav"])
    {
    }
    else
    {
        config["nav"] = {}
        config["nav"]["state"] = {};
    }


    if ("nav" in config && "state" in config["nav"])
    {
        for (let item of document.querySelectorAll(".nav-item"))
        {
            console.log("LOOP");
            if (item.getAttribute('data-nav-item-name') in config["nav"]["state"])
            {
                if (config["nav"]["state"][item.getAttribute('data-nav-item-name')]["expanded"] === "yes")
                {
                    console.log("YES!!");
                    item.classList.add('nav-item-expanded');
                } 
                else 
                {
                    console.log("NO!!");
                    item.classList.remove('nav-item-expanded');
                }
            }

        }

        //for (let item in config["side-nav"]["state"])
        //{
        //    if (config["side-nav"]["state"][item]["expanded"] === "yes")
        //    {
        //        console.log("YES!!");
        //        document.querySelector("#" + item).classList.add('expanded');
        //    } 
        //    else 
        //    {
        //        console.log("NO!!");
        //        document.querySelector("#" + item).classList.remove('expanded');
        //    }

        //    //console.log(config["side-nav"]["state"][item]["expanded"]);
        //}
        console.log("Config:");
        console.log(config);
    }

    for (let item of document.querySelectorAll(".nav-item"))
    {
        if (item.getAttribute('data-nav-item-name') == document.body.getAttribute('data-nav-item-name')) 
        item.classList.add("nav-item-active");
    }
 
    //if (document.querySelector("." + document.body.getAttribute('data-nav-item-name')))
    //{
    //    document.querySelector("." + document.body.getAttribute('data-nav-item-name')).classList.add("nav-item-active");
    //    console.log("nav-item-active");
    //}

}


document.addEventListener('DOMContentLoaded', function() {
  //setActive();
    load();
});

    //let config = {};

    //config["side-nav"] = {};
    //config["side-nav"]["state"] = {};
    //config["side-nav"]["state"]["side-nav-item--root-products-jay40"] = {};
    //config["side-nav"]["state"]["side-nav-item--root-products-jay40"]["expanded"] = "yes";
    //config["side-nav"]["state"]["side-nav-item--root-products-jaybtn"] = {};
    //config["side-nav"]["state"]["side-nav-item--root-products-jaybtn"]["expanded"] = "no";

    //localStorage.setItem('config', JSON.stringify(config));



//function setNewActive() {
//    this.parentElement.classList.toggle('active');
//    console.log("setActive");
//    console.log("setActive");
//}

for (let sideNavButtonChevron of document.querySelectorAll('.nav-button-chevron')) {
    sideNavButtonChevron.addEventListener('click', toggleExpanded); 
}

for (let sideNavButtonText of document.querySelectorAll('.nav-button-text')) {
    //sideNavButtonLabel.addEventListener('click', setActive); 
    sideNavButtonText.addEventListener('click', navButtonClick); 
}

for (let navButtonLabel of document.querySelectorAll('.nav-button')) {
    //sideNavButtonLabel.addEventListener('click', setActive); 
    navButtonLabel.addEventListener('click', navButtonClick); 
    //console.log(navButtonLabel)
}

for (let item of document.querySelectorAll('.nav-hamburger-button')) {
    item.addEventListener('click', addNavExpanded); 
}

for (let item of document.querySelectorAll('.nav-cross-button')) {
    item.addEventListener('click', removeNavExpanded); 
}

for (let item of document.querySelectorAll('.product-gallery-thumbnail')) {
    item.addEventListener('click', setDisplayImage); 
}

//for (let sideNavButton of sideNavButtons) {
//    sideNavButton.addEventListener('click', toggleExpanded); 
//    sideNavButton.addEventListener('click', setActive); 
//}

//for (let sideNavItem of sideNavItems) {
//    sideNavItem.addEventListener('click', function() {
//        //this.style.backgroundColor = "red";
//        console.log("Clicked.")
//        this.classList.toggle('expanded');
//        
//        // Save state after toggling
//        //saveExpandedState();
//    });
//}


