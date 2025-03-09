document.addEventListener("DOMContentLoaded", function() {
    console.log("menu.js loaded");  // Debugging log

    let menuList = document.getElementById("menuList");
    let menuIcon = document.querySelector(".menu-icon i");

    function ToggleMenu() {
        console.log("Menu Toggled"); // Check if function runs
        menuList.classList.toggle("show-menu"); // Toggle class for visibility
    }

    if (menuIcon) {
        menuIcon.addEventListener("click", ToggleMenu);
    } else {
        console.error("Menu icon not found in DOM");
    }
});
