
const mobile_menu_button = document.getElementById("mobile-menu-button");
const mobile_menu_close = document.getElementById("list-menu-close");
const mobile_menu = document.getElementById("list-menu-mobile");

const mobile_header_open_btn = document.getElementById("header-right-mobile-button")
const mobile_header_close_btn = document.getElementById("mobile-header-close-button");
const mobile_header_menu = document.getElementById("mobile-header-menu");

mobile_menu_button.addEventListener("click", function() {
    mobile_menu.style.display = "block";
});

mobile_menu_close.addEventListener("click", function() {
    mobile_menu.style.display = "none";
});

mobile_header_open_btn.addEventListener("click", function() {
    mobile_header_menu.style.display = "flex";
})

mobile_header_close_btn.addEventListener("click", function() {
    mobile_header_menu.style.display = "none";
})