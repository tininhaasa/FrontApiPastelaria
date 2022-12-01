/**
*
* Script do login de admin
*
* @author Emprezaz
*
**/
(function($, PATH, Helpers){

    // Verificando a senha
    var checkPasswordInDatabase = (login, password) => {

        var checkPassword;

        $.ajax({
            url: PATH + '/checkPasswordAdm',
            dataType: 'json',
            type: 'POST',
            async: false,
            data: {
                login: login,
                password: password,
            },
            complete: function(response){

                checkPassword = response.responseJSON.result;

            }
        });

        return checkPassword;

    }

    // Verificando o nome de usuário
    var checkLoginInDatabase = (login) => {

        var checkLogin;

        $.ajax({
            url: PATH + '/checkLoginAdm',
            dataType: 'json',
            type: 'POST',
            async: false,
            data: {
                login: login,
            },
            complete: function(response){
                checkLogin = response.responseJSON.result;
            }
        });

        return checkLogin;

    }
    // Verificando o email do usuário
    var checkEmailInDatabase = (email) => {

        var checkUser;

        $.ajax({
            url: PATH + '/checkEmailAdm',
            dataType: 'json',
            type: 'POST',
            async: false,
            data: {
                email: email,
            },
            complete: function(response){
                checkUser = response.responseJSON.result;
            }
        });

        return checkUser;

    }

    // Validação dos campos
    var validateFields = () => {

        var login = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();

        if(login == ''){

            swal({
                type: 'error',
                title: 'Erro - Login',
                text: 'Preencha o nome de usuário',
            });
            return false;

        }

        if(password == ''){

            swal({
                type: 'error',
                title: 'Erro - Login',
                text: 'Preencha sua senha'
            });
            return false;

        }

        return true;

    }

    // Função parar executar o login
    var login = () => {

        $('body').on('click', '.btn-login', function(){

            if(validateFields()){

                $.ajax({
                    url: PATH + 'login_usuario/',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        matricula: $('#login').val(),
                        senha: $('#senha').val()
                    }
                }).done(function(res){
                    console.log(res)
                    if(typeof res[0].id !== "undefined"){
                        
                        window.location.href = PATH + 'home';
                    }else{
                        
                        Swal.fire({
                            icon: 'error',
                            text: res[0].erro,
                            confirmButtonText: "Continuar",
                            confirmButtonColor: "#ffc107"
                        }).then(function (res) {
                            return false;
                        })
                    }
                });

            }


        });

    }

    //Validação de email para envio de link ao email do admnistrador
	$( document ).ready(function(){
        login();
    });

})($, PATH, Helpers);