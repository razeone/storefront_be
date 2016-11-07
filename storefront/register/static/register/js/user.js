function User(email, password, confirm) {
    /*
    The User class for register and other stuff
    */
    
    // The constructor
    this.email = email;
    this.password = password;
    this.confirm = confirm;
    this.errors = [];

    // The endpoint for user creation
    var validEndpoint = '/register/customer/'

    // Email validation through JS and regex
    this.validateEmail = function() {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }

    // Easy password validation
    this.validatePassword = function() {
        if(this.password != this.confirm) {
            this.errors.push('Las contraseñas ingresadas no coinciden');
        }
        else {
            if(this.password.length < 8) {
                this.errors.push('El password debe al menos contener 8 caracteres');
            }
        }
    }

    // Validate all fields and fill error messages
    this.validate = function() {
        if(this.email == '' || this.password == '' || this.confirm == '') {
            this.errors.push('Todos los valores son requeridos');
        }
        if(!this.validateEmail()) {
            this.errors.push('El correo electrónico no parece tener formato válido');
        }
        this.validatePassword();
        
        if(this.errors.length == 0) {
            return true;
        }
        else {
            return false;
        }
    }

    // Display error messages
    this.displayErrors = function() {
        $('#error-messages').html('');
            for(error in this.errors) {
                $('#error-messages').append('<li>' + this.errors[error] + '</li>');
            }
        $('#error-messages').fadeIn();
    }

    // Create the user
    this.create = function() {
        var userData = {
            email: this.email,
            password: this.password
        };

        // Getting CSRF
        var csrftoken = $.cookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            });

        $.ajax({
            url: validEndpoint,
            method: "POST",
            data: userData
        })
        .done(function(res) {
            // Success
            $("#success-messages").html('El usuario se ha creado correctamente');
            $("#success-messages").fadeIn();
        })
        .fail(function(res) {
            // Errors
            for(error in res.responseJSON) {
                $("#error-messages").html(res.responseJSON[error]);    
            }
            $("#error-messages").fadeIn();
        });
    }
}