function adoptionValidation(event) {
            
    // the variables for each part of them using the respective id
    var animal = document.getElementById('animal');
    var petForm = document.getElementById('petForm');
    var textDescribe = document.getElementById('textDescribe');
    var anyPets = document.getElementsByName('any_pets');
    var yesNo = document.getElementsByName('yes_no')

    var messages = []

    // the variables for each error
    var error = document.getElementById('error');
    var error2 = document.getElementById('error2');
    var error3 = document.getElementById('error3');
    var error4 = document.getElementById('error4');

    // regular expression pattern to prevent inappropriate characters
    var petPattern = /^[A-Za-z]+$/;
    
    // validates the pet name form question
    if(animal.value.trim() === '' || animal.value === null) {
        animal.style.borderColor = 'red'
        messages.push('The name of the pet is required')
        error.textContent = 'The name of the pet is required'
    } else if(!petPattern.test(animal.value)) {
        animal.style.borderColor = 'red'
        messages.push('Only letters allowed')
        error.textContent = 'Only letters allowed'
    }  else {
        error.textContent = '' // Clear the error message
        animal.style.borderColor = ''
    }   
    
    // validates the pets radio button question, makes sure you have an option selected
    var anyPetsSelected = false;
    for(var i = 0; i < anyPets.length; i++) {
        if(anyPets[i].checked) {
            anyPetsSelected = true;
        }
    }

    if(!anyPetsSelected) {
        messages.push('Please select an option')
        error2.textContent ='Please select an option'
    } else {
        error2.textContent = '' // Clear the error message
    }

    // validates the children radio button question, makes sure you have an option selected
    var yesNoSelected = false;
    for(var i = 0; i < yesNo.length; i++) {
        if(yesNo[i].checked) {
            yesNoSelected = true;
        }
    }

    if(!yesNoSelected) {
        messages.push('Please select an option')
        error3.textContent ='Please select an option'
    } else {
        error3.textContent = '' // Clear the error message
    }

    // validates the home details form question
    if(textDescribe.value.trim() === '' || textDescribe.value === null) {
        textDescribe.style.borderColor = 'red'
        messages.push('Details about your home are required')
        error4.textContent = 'Details about your home are required'
    } else {
        error4.textContent = '' // Clear the error message
        textDescribe.style.borderColor = ''
    }
    
    // prevents the form from being submitted if any of the messages have been pushed
    if(messages.length > 0) {
        event.preventDefault();
    }    
}