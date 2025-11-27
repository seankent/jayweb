
//const sideNavButtons = document.querySelectorAll('.side-nav-button');

function toggleExpanded() {
    this.parentElement.parentElement.classList.toggle('expanded');
    console.log("toggleExpanded.");
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
    localStorage.setItem('username', 'Sean');
    console.log("Navigating!!");
    console.log(localStorage.getItem('username'));
}

function setActive() {
    console.log("New Page");

    const currentPath = window.location.pathname;

    for (let link of document.querySelectorAll('.side-nav-button-label')) {
        if (currentPath.endsWith(link.getAttribute('href'))) {
            //link.classList.add('active');
            console.log("TRUE!!!");
            link.classList.add('active');
        }
    }
    //console.log(window.location.pathname);
}

document.addEventListener('DOMContentLoaded', function() {
  setActive();
});

//function setNewActive() {
//    this.parentElement.classList.toggle('active');
//    console.log("setActive");
//    console.log("setActive");
//}

for (let sideNavButtonChevron of document.querySelectorAll('.side-nav-button-chevron')) {
    sideNavButtonChevron.addEventListener('click', toggleExpanded); 
}

for (let sideNavButtonLabel of document.querySelectorAll('.side-nav-button-label')) {
    //sideNavButtonLabel.addEventListener('click', setActive); 
    sideNavButtonLabel.addEventListener('click', navButtonClick); 
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


