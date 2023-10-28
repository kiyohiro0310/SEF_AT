
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

// Validation field
const form = document.getElementById("pet-form");

if (form) {
    form.addEventListener("submit", function(event) {
        const pet_name = document.getElementById("pet-name");
        const pet_name_err = document.getElementById("pet-name-err");

        const species = document.getElementById("species");
        const species_err = document.getElementById("species-err");

        const breed = document.getElementById("breed");
        const breed_err = document.getElementById("breed-err");

        const age = document.getElementById("age");
        const age_err = document.getElementById("age-err");

        const suburb = document.getElementById("suburb");
        const suburb_err = document.getElementById("suburb-err");

        const fee = document.getElementById("fee");
        const fee_err = document.getElementById("fee-err");

        const description = document.getElementById("description");
        const description_err = document.getElementById("description-err");

        const submit_err = document.getElementById("submit-err");

        if (pet_name.value == '' || pet_name.value.test(/^[A-Za-z]+$/)) {
            pet_name_err.style.display = "block";
            pet_name.style.borderColor = "red";
            submit_err.style.display = "block";
            event.preventDefault();
        }

        if (species.value == '' || species.value.test(/^[A-Za-z]+$/)) {
            species_err.style.display = "block";
            submit_err.style.display = "block";
            species.style.borderColor = "red";
            event.preventDefault();
        }

        if (breed.value == '' || breed.value.test(/^[A-Za-z]+$/)) {
            breed_err.style.display = "block";
            submit_err.style.display = "block";
            breed.style.borderColor = "red";
            event.preventDefault();
        }

        if (age.value == '' || age.value.test(/^[A-Za-z]+$/)) {
            age_err.style.display = "block";
            submit_err.style.display = "block";
            age.style.borderColor = "red";
            event.preventDefault();
        }

        if (suburb.value == '' || suburb.value.test(/^[A-Za-z]+$/)) {
            suburb_err.style.display = "block";
            submit_err.style.display = "block";
            suburb.style.borderColor = "red";
            event.preventDefault();
        }

        if (fee.value == '' || fee.value.test(/^[A-Za-z]+$/)) {
            fee_err.style.display = "block";
            submit_err.style.display = "block";
            fee.style.borderColor = "red";
            event.preventDefault();
        }

        if (description.value == '' || description.value.test(/^[A-Za-z]+$/)) {
            description_err.style.display = "block";
            submit_err.style.display = "block";
            description.style.borderColor = "red";
            event.preventDefault();
        }
    });
}