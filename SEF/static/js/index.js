const mobile_header_open_btn = document.getElementById("header-right-mobile-button")
const mobile_header_close_btn = document.getElementById("mobile-header-close-button");
const mobile_header_menu = document.getElementById("mobile-header-menu");

mobile_header_open_btn.addEventListener("click", function() {
    mobile_header_menu.style.display = "flex";
})

mobile_header_close_btn.addEventListener("click", function() {
    mobile_header_menu.style.display = "none";
})