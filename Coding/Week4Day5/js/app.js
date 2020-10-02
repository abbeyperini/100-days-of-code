// Password must be at least 4 characters, no more than 8 characters, and must include at least one upper case letter, one lower case letter, and one numeric digit.

var firstName = document.getElementById('firstName');
var lastName = document.getElementById('lastName');
var email = document.getElementById('email');
var password = document.getElementById('password');

firstName.oninvalid = function(event) {
    event.target.setCustomValidity('First name must contain only letters, a single hyphen, and a single space.');
}

lastName.oninvalid = function(event) {
    event.target.setCustomValidity('Last name must contain only letters, a single hyphen, and a single space.');
}

email.oninvalid = function(event) {
    event.target.setCustomValidity('Not a valid email.');
}

password.oninvalid = function(event) {
    event.target.setCustomValidity('Password must be at least 4 characters, no more than 8 characters, and must include at least one upper case letter, one lower case letter, and one numeric digit.');
}