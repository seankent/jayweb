
//const sideNavButtons = document.querySelectorAll('.side-nav-button');

function toggleExpanded() {
    this.parentElement.parentElement.classList.toggle('expanded');
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

    config["side-nav"] = "Sean";
    localStorage.setItem('config', JSON.stringify(config));
    
    console.log(sideNav.id);
    console.log(config["side-nav"]);

    config = JSON.parse(localStorage.getItem('config'));
    console.log(config);


}

function store()
{
    console.log("[INFO] Running 'store()'");

    let config = JSON.parse(localStorage.getItem('config') || '{}');

    if (!("side-nav" in config))
    {
        config["side-nav"] = {};
    }

    if (document.querySelector('.side-nav'))
    {
        config["side-nav"]["side-nav-group"] = document.querySelector('.side-nav').id;
    }
    else
    {
        config["side-nav"]["side-nav-group"] = "none";
    }

    if (!("state" in config["side-nav"]))
    {
        config["side-nav"]["state"] = {};
    }

    for (let item of document.querySelectorAll(".side-nav-item"))
    {
        if (!(item.id in config["side-nav"]["state"]))
        {
            config["side-nav"]["state"][item.id] = {};
        }

        if (item.classList.contains("expanded"))
        {
            config["side-nav"]["state"][item.id]["expanded"] = "yes";
        }
        else
        {
            config["side-nav"]["state"][item.id]["expanded"] = "no";
        }
    }

    localStorage.setItem('config', JSON.stringify(config));
}

function load()
{
    console.log("[INFO] Running 'load()'");

    let config = JSON.parse(localStorage.getItem('config') || '{}');


    if ("side-nav" in config && "side-nav-group" in config["side-nav"])
    {
        
        if (document.querySelector('.side-nav'))
        {
            if (config["side-nav"]["side-nav-group"] !== document.querySelector('.side-nav').id)
            {
                config["side-nav"]["state"] = {};
            }

        }
        else
        {
            config["side-nav"]["state"] = {};
        }
        if (config["side-nav"]["side-nav-group"] === "none") 
        {
            config["side-nav"]["state"] = {};
        }
    }

    if ("side-nav" in config && "state" in config["side-nav"])
    {
        for (let item of document.querySelectorAll(".side-nav-item"))
        {
            if (item.id in config["side-nav"]["state"])
            {
                //console.log(item.id);
                if (config["side-nav"]["state"][item.id]["expanded"] === "yes")
                {
                    console.log("YES!!");
                    item.classList.add('expanded');
                } 
                else 
                {
                    console.log("NO!!");
                    item.classList.remove('expanded');
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
 
    if (document.querySelector("#" + document.body.getAttribute('data-active-side-nav-item')))
    {
        document.querySelector("#" + document.body.getAttribute('data-active-side-nav-item')).classList.add("active");
    }

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

for (let sideNavButtonChevron of document.querySelectorAll('.side-nav-button-chevron')) {
    sideNavButtonChevron.addEventListener('click', toggleExpanded); 
}

for (let sideNavButtonText of document.querySelectorAll('.side-nav-button-text')) {
    //sideNavButtonLabel.addEventListener('click', setActive); 
    sideNavButtonText.addEventListener('click', navButtonClick); 
}

for (let navButtonLabel of document.querySelectorAll('.nav-button')) {
    //sideNavButtonLabel.addEventListener('click', setActive); 
    navButtonLabel.addEventListener('click', navButtonClick); 
    //console.log(navButtonLabel)
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


