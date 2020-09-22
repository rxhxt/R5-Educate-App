var nameInput = document.getElementById('name');
var emailInput = document.getElementById('email');
var passwordInput = document.getElementById('password');
var passwordInputConfirm = document.getElementById('passwordCon');
var selectInput = document.getElementById('exampleFormControlSelect1');
var loginPasswordInput = document.getElementById('loginPassword')
var loginemailInput = document.getElementById('loginemail');


//for signup
document.querySelector('form.signup-form').addEventListener('submit', function(e) {

    //prevent the normal submission of the form
    e.preventDefault();
    console.log(selectInput.value);
    console.log(nameInput.value);
    console.log(emailInput.value);
    console.log(passwordInput.value);
    console.log(passwordInputConfirm.value);

    var data = {
        id: 0,
        selectInput_d : selectInput.value,
        nameInput_d : nameInput.value,
        emailInput_d: emailInput.value,
        passwordInput_d: passwordInput.value,
        passwordInputConfirm_d: passwordInputConfirm.value
    };
    fetch(`${window.origin}/`,{
        method:"POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

});
document.querySelector('form.login-form').addEventListener('submit', function(e) {

    //prevent the normal submission of the form
    e.preventDefault();
    console.log(loginemailInput.value);
    console.log(loginPasswordInput.value);

    var data = {
        id: 1,
        loginemailInput_d: loginemailInput.value,
        loginPasswordInput_d: loginPasswordInput.value,
    };
    console.log(data)
    fetch(`${window.origin}/`,{
        method:"POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

});