/*Formulario Validacion */
// Defining a function to display error message
function printError(elemId, hintMsg) {
    document.getElementById(elemId).innerHTML = hintMsg;
}

// Defining a function to validate form 
function validateForm() {
    // Retrieving the values of form elements 
    var name = document.contactForm.name.value;
    var email = document.contactForm.email.value;
    var mobile = document.contactForm.mobile.value;
    var country = document.contactForm.country.value;
    var gender = document.contactForm.gender.value;

    // Defining error variables with a default value
    var nameErr = emailErr = mobileErr = countryErr = genderErr = true;

    // Validate name
    if (name == "") {
        printError("nameErr", "Por Favor Ingrese su nombre ");
    } else {
        var regex = /^[a-zA-Z\s]+$/;
        if (regex.test(name) === false) {
            printError("nameErr", "Por Favor Ingresa un nombre valido");
        } else {
            printError("nameErr", "");
            nameErr = false;
        }
    }

    // Validate email address
    if (email == "") {
        printError("emailErr", "Por Favor Ingrese Su Correo");
    } else {
        // Regular expression for basic email validation
        var regex = /^\S+@\S+\.\S+$/;
        if (regex.test(email) === false) {
            printError("emailErr", "Por Favor Ingrese un Correo Valido");
        } else {
            printError("emailErr", "");
            emailErr = false;
        }
    }

    // Validate mobile number
    if (mobile == "") {
        printError("mobileErr", "Por Favor Ingrese Su Numero Telefonico");
    } else {
        var regex = /^[1-9]\d{9}$/;
        if (regex.test(mobile) === false) {
            printError("mobileErr", "Por favor Ingrese un Numero Valido(+569)12345678");
        } else {
            printError("mobileErr", "");
            mobileErr = false;
        }
    }

    // Validate country
    if (country == "seleccionar") {
        printError("countryErr", "Por Favor Ingrese Su Region");
    } else {
        printError("countryErr", "");
        countryErr = false;
    }

    // Validate gender
    if (gender == "") {
        printError("genderErr", "Por Favor Ingrese Su Genero");
    } else {
        printError("genderErr", "");
        genderErr = false;
    }

    // Prevent the form from being submitted if there are any errors
    if ((nameErr || emailErr || mobileErr || countryErr || genderErr) == true) {
        return false;
    } else {
        // Creating a string from input data for preview
        var dataPreview = "Tu Has Ingresado los siguientes Datos: \n" +
            "Nombre Completo: " + name + "\n" +
            "Correo: " + email + "\n" +
            "Telefono: " + mobile + "\n" +
            "Region: " + country + "\n" +
            "Genero: " + gender + "\n";
    }
    // Display input data in a dialog box before submitting the form
    alert(dataPreview);
};