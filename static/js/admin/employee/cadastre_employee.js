(function ($, PATH, Helpers) {

    var masks = function () {
        Helpers.cpfcnpjMask($('#document'));
        Helpers.phoneMask($('#phone'));
    }

    var check = function(){

        var name        = $('#name').val().trim();
        var document    = $('#document').val().trim();
        var phone       = $('#phone').val().trim();
        var group       = $('#group').val();
        var login       = $('#login').val().trim();
        var pass        = $('#password').val().trim();
        var repass      = $('#repass').val().trim();

        if(name == ""){
            Swal.fire({
                icon: 'error',
                text: 'Insira o nome do funcionário',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(document == ""){
            Swal.fire({
                icon: 'error',
                text: 'Insira o documento do funcionário',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(phone == ""){
            Swal.fire({
                icon: 'error',
                text: 'Insira o telefone do funcionário',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(group == ""){
            Swal.fire({
                icon: 'error',
                text: 'Selecione o grupo que esse usuário participa',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(login == ""){
            Swal.fire({
                icon: 'error',
                text: 'Insira o login para o funcionário',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(pass == ""){
            Swal.fire({
                icon: 'error',
                text: 'Insira a senha de acesso',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(repass == ""){
            Swal.fire({
                icon: 'error',
                text: 'Confirme a senha inserida',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if(pass != repass){
            Swal.fire({
                icon: 'error',
                text: 'As duas senhas devem ser iguais',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }

        return true;
    }

    var save = function(){
        $("body").on("click", "#save", function(){
            if(check()){
                Swal.fire({
                    icon: 'success',
                    text: 'Funcionário cadastrado com sucesso',
                    confirmButtonText: "Continuar",
                    confirmButtonColor: "#ffc107"
                }).then(function(res){
                    window.location.href = PATH + '/funcionario'
                })
            }
        })
    }
    
    $(document).ready(function () {
        $('#name').focus()
        masks();
        save();
    });

})($, PATH, Helpers);