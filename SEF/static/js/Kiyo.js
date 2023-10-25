
const mobile_menu_button = document.getElementById("mobile-menu-button");
const mobile_menu_close = document.getElementById("list-menu-close");
const mobile_menu = document.getElementById("list-menu-mobile");

const mobile_header_open_btn = document.getElementById("header-right-mobile-button")
const mobile_header_close_btn = document.getElementById("mobile-header-close-button");
const mobile_header_menu = document.getElementById("mobile-header-menu");

if (mobile_menu_button) {
    mobile_menu_button.addEventListener("click", function() {
        mobile_menu.style.display = "block";
    });
}

if (mobile_menu_close) {
    mobile_menu_close.addEventListener("click", function() {
        mobile_menu.style.display = "none";
    });
}

if (mobile_header_open_btn) {
    mobile_header_open_btn.addEventListener("click", function() {
        mobile_header_menu.style.display = "flex";
    })
}

if (mobile_header_close_btn) {
    mobile_header_close_btn.addEventListener("click", function() {
        mobile_header_menu.style.display = "none";
    })
}