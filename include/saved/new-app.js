function load()
{
    return JSON.parse(localStorage.getItem('config') || '{}');
}

function store(config)
{
    console.log(config);
    localStorage.setItem('config', JSON.stringify(config));
}

function init()
{
    let config = JSON.parse(localStorage.getItem('config') || '{}');
    
    if (Object.keys(config).length === 0)
    {
        config["display"] = {};
        config["display"]["nav-menu"] = "no";
    }

    localStorage.setItem('config', JSON.stringify(config));

    console.log("Init Done")
    console.log(config)
    //debugger;
}

function remToPx(rem)
{
    return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
}


function addNavMenu() {
    let config = load(); 

    config["display"]["nav-menu"] = "yes";

    store(config);
    display();
    //debugger;
}

function removeNavMenu() {
    let config = load(); 

    config["display"]["nav-menu"] = "no";

    store(config);
    display();
    //debugger;
}


function display()
{
    let config = JSON.parse(localStorage.getItem('config') || '{}');


    document.body.className = '';

    if (config["display"]["nav-menu"] === "yes")
    {
        document.body.classList.add('body-two');
    } 
    else
    {
        document.body.classList.add('body-one');
    }

    //if (window.innerWidth <= remToPx(58))
    //{
    //    console.log('Mobile view');
    //    // Do mobile-specific stuff
    //    document.body.classList.add('body-two');
    //} 
    //else 
    //{
    //    console.log('Desktop view');
    //    // Do desktop-specific stuff
    //    document.body.classList.add('body-one');
    //}
}

// Run on page load
init();
display();

// Run whenever the window is resized
window.addEventListener('resize', display);



for (let element of document.querySelectorAll('.nav-hamburger-button')) {
    element.addEventListener('click', addNavMenu); 
}

for (let element of document.querySelectorAll('.nav-cross-button')) {
    element.addEventListener('click', removeNavMenu); 
}



