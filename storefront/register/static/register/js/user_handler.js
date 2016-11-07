$(function(){
    
    $( "#register-form" ).submit(function( event ) {
        event.preventDefault();
        var email = $('#email-register').val();
        var password = $('#password-register').val();
        var confirm = $('#confirm-register').val();
        var newUser = new User(email, password, confirm);
        if(newUser.validate()) {
            newUser.create();
        }
        else {
            newUser.displayErrors();
        }
    });
});