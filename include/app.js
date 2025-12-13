function load()
{
    let config = JSON.parse(localStorage.getItem('config') || '{}');

    if (JSON.stringify(config) === '{}')
    {
        config["nav"] = {};
    }

    console.log(config);
    return config
}

function store(config)
{
    console.log(config);
    localStorage.setItem('config', JSON.stringify(config));
}


function save()
{
    console.log("[INFO] Saving state.");

    let config = load() ;

    for (let element of document.querySelectorAll(".nav-item"))
    {
        if (element.classList.contains("show"))
        {
            config["nav"][element.id] = "yes";
        }
        else
        {
            config["nav"][element.id] = "no";
        }
    }

    store(config);
}


function restore()
{
    console.log("[INFO] Restoring state.");

    let config = load() ;

    for (let element of document.querySelectorAll(".nav-item"))
    {
        if (element.id in config["nav"] && config["nav"][element.id] === "yes")
        {
            element.classList.add('show');
        }

        if (element.getAttribute('data-page-id') == document.body.getAttribute('data-page-id')) 
        {
            element.classList.add("active");
        }

    }
}


function addNavMenuExpanded() {
    this.parentElement.classList.add('show');
    document.body.classList.add('show');
}

function removeNavMenuExpanded() {
    this.parentElement.classList.remove('show');
    document.body.classList.remove('show');
}

function toggleNavExpanded() {
    this.parentElement.parentElement.classList.toggle('show');
}

function navButtonClick() {
    save();
}



for (let element of document.querySelectorAll('.nav-hamburger-button')) {
    element.addEventListener('click', addNavMenuExpanded); 
}

for (let element of document.querySelectorAll('.nav-cross-button')) {
    element.addEventListener('click', removeNavMenuExpanded); 
}

for (let element of document.querySelectorAll('.nav-button-chevron')) {
    element.addEventListener('click', toggleNavExpanded); 
}

for (let element of document.querySelectorAll('.nav-button')) {
    element.addEventListener('click', navButtonClick); 
}

// Save state whenever leaving page
window.addEventListener('pagehide', () => {
    save();
});

// Restore on load
window.addEventListener('pageshow', () => {
    restore()
});
