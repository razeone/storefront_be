function User(email, password, confirm) {
    /*
    The User class for register and other stuff
    */
    
    // The constructor
    this.email = email;
    this.password = password;
    this.confirm = confirm;
    this.errors = [];
    this.success = [];
    var validEndpoint = '/register/customer/'

    this.validateEmail = function() {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }

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

    this.displayErrors = function() {
        $('#error-messages').html('');
            for(error in this.errors) {
                $('#error-messages').append('<li>' + this.errors[error] + '</li>');
            }
        $('#error-messages').fadeIn();
    }


    this.create = function() {
        console.log('Create');
        var userData = {
            email: this.email,
            password: this.password
        };

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
            if(res.status == 201) {
                this.success.push('El usuario se ha creado correctamente');
                return true;
            }
        })
        .fail(function(res) {
            this.errors.push(res.responseText);
            return false;
        });
    }
}