const form = document.getElementById('form')
const firstName = document.getElementById('firstName')
const lastName = document.getElementById('lastName')
const email = document.getElementById('email')
const phone = document.getElementById('phone')
var regExpForPhone = /^[0-9]{10}$/;


/*form.addEventListener('submit', (e) => {
    let messages = []
    if (firstName.value === '' || firstName.value == null){
        messages.push('Name is requried')
    }

    if(lastName.value.length >= 5){
        messages.push('Teest change last name to less then 5.')
    }

    if(messages.length > 0){
    e.preventDefault()
}
})*/

function RegExp(){
    var formString = document.getElementById("name").value;
    var regularExpress = "/^[A-Z a-z{}$/";
    if(regularExpress.test(formString)){
        alert("Correct, this is valid.");
    }
    else{
        alert("Error there are numbers, please only letters")
    }
}