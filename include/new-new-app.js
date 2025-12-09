function load()
{
    return JSON.parse(localStorage.getItem('config') || '{}');
}

function store(config)
{
    console.log(config);
    localStorage.setItem('config', JSON.stringify(config));
}

function addNavMenuExpanded() {
    this.parentElement.parentElement.classList.add('expanded');
}

function removeNavMenuExpanded() {
    this.parentElement.parentElement.classList.remove('expanded');
}

function toggleNavExpanded() {
    this.parentElement.parentElement.classList.toggle('expanded');
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



