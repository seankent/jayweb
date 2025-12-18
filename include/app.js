// Use a Map to store separate timeouts for each element
let scrollTimeouts = new Map();


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

function setDisplayImage() {
    let element = document.querySelector('.product-gallery-image img');
    element.src = this.querySelector('img').src;
}

//function showScrollbar(e) {
//    let element = e.target;
//    element.classList.add('is-scrolling');
//}
//
//function hideScrollbar(e) {
//    let element = e.target;
//    element.classList.remove('is-scrolling');
//}


function handleScroll(e) {
//    let element = e.target;
//    element.classList.add('is-scrolling');
//
//    // Clear existing timeout for THIS specific element
//    if (scrollTimeouts.has(element)) {
//        clearTimeout(scrollTimeouts.get(element));
//    }
//
//    //scrollTimeout = setTimeout(() => {
//    //    element.classList.remove('is-scrolling');
//    //}, 500);
//
//
//    // Create new timeout for THIS specific element
//    const timeout = setTimeout(() => {
//        element.classList.remove('is-scrolling');
//        //scrollTimeouts.delete(scrollingElement); // Clean up
//    }, 1000);
//
//    // Store the timeout with the element as the key
//    scrollTimeouts.set(element, timeout);
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

for (let element of document.querySelectorAll('.product-gallery-thumbnail')) {
    element.addEventListener('click', setDisplayImage); 
}

// Save state whenever leaving page
window.addEventListener('pagehide', save);
//window.addEventListener('pagehide', () => {
//    save();
//});

// Restore on load
window.addEventListener('pageshow', restore);
//window.addEventListener('pageshow', () => {
//    restore();
//});


document.addEventListener('scroll', handleScroll, true);

//document.addEventListener('scroll', () => {
//    showScrollbar();
//    console.log("Window scroll detected");
//}, true);


const { OverlayScrollbars, ClickScrollPlugin } = OverlayScrollbarsGlobal;

// optional: use the ClickScrollPlugin to make the option "scrollbars.clickScroll: true" available
OverlayScrollbars.plugin(ClickScrollPlugin);

OverlayScrollbars(document.body, {
    scrollbars: {
        clickScroll: true,
        visibility: 'auto',
        //visibility: 'hover',
        //visibility: 'visible',
        //autoHide: 'move',
        autoHide: 'scroll',
        autoHideDelay: 1000,
    },
});

//OverlayScrollbars(document.querySelector('.nav'), {
//    scrollbars: {
//        clickScroll: true,
//        visibility: 'auto',        // Change from 'visible' to 'auto'
//        autoHide: 'leave',         // Change from 'never' to 'leave', 'scroll', or 'move'
//        autoHideDelay: 1000,       // Delay in ms before hiding (default is 1300)
//    },
//});


//OverlayScrollbars(document.getElementById('target'), {});

//OverlayScrollbars(document.getElementById('target'), {});
//OverlayScrollbars(document.body, {});
