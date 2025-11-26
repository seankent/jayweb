
const sideNavButtons = document.querySelectorAll('.side-nav-button');

function toggleExpanded() {
    this.parentElement.classList.toggle('expanded');
    console.log("Clicked.");
}

for (let sideNavButton of sideNavButtons) {
    sideNavButton.addEventListener('click', toggleExpanded); 
}

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


