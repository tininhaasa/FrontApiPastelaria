(function ($, PATH, Helpers) {

    var masks = function () {
        Helpers.moneyMask($('#price'))
    }

    var clickphoto = function () {
        $('body').on('mouseup', '.img-product', function () {

            $('#image_product').click();
        });
        $('body').on('change', '#image_product', function () {

            var input = this;
            var check = true;

            // atribuição de extensão e formato de arquivo
            var file = this.files[0].size;
            var file = Math.round((file / 1024));
            var extension = this.files[0].type;

            if (extension != 'image/png' && extension != 'image/jpeg' && extension != 'image/jpg') {
                swal('Erro', 'Extensão de arquivo não suportada', 'error');
                $(this).val(null);
                check = false;
            }

            if (check) {
                if (input.files && input.files[0]) {
                    var reader = new FileReader();

                    reader.onload = function (e) {
                        $('.img-product').attr('style', 'background-image: url(' + e.target.result + ');background-size:cover');

                    }

                    reader.readAsDataURL(input.files[0]);
                }
            }

        });
    }

    var check = function () {
        var name = $('#name').val().trim();
        var price = $('#price').val().trim();
        var qtd = $('#qtd').val().trim();

        if (name == "") {
            Swal.fire({
                icon: 'error',
                text: 'Insira o nome do produto',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if (price == "") {
            Swal.fire({
                icon: 'error',
                text: 'Insira o preço do produto',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }
        if (qtd == "") {
            Swal.fire({
                icon: 'error',
                text: 'Insira a quantidade do produto',
                confirmButtonText: "Continuar",
                confirmButtonColor: "#ffc107"
            })
            return false;
        }

        return true;
    }

    var save = function () {
        $('body').on('click', "#save", function () {
            if (check()) {
                
                $('#product-form').submit(function(e){
                    
                    var formObj = $(this);
                    var formURL = formObj.attr("action");
                    var formData = new FormData(this);

                    formData.delete('price');

                    var price = $("#price").val().replace('R$', '');
                    price = price.replace('.', '');
                    price = price.replace(',', '.');

                    formData.append("price", price);
                    console.log($("#id").val())
                    if($("#id").val() != "0" && $("#id").val() != ""){
                        $.ajax({
                            url: PATH + 'produto/editar_produto/',
                            data: formData,
                            type: 'POST',
                            dataType: 'json',
                            mimeType: "multipart/form-data",
                            contentType: false,
                            cache: false,
                            processData: false,
                            async: false,
                        }).done(function(res) {

                            array_res = res[0];
                            if(typeof res[0].erro != "undefined"){
                                Swal.fire({
                                    icon: 'error',
                                    text: res[0].erro,
                                    confirmButtonText: "Continuar",
                                    confirmButtonColor: "#ffc107"
                                }).then(function () {
                                    return false;
                                })
                            } else {
                                Swal.fire({
                                    icon: 'success',
                                    text: 'Produto cadastrado com sucesso',
                                    confirmButtonText: "Continuar",
                                    confirmButtonColor: "#ffc107"
                                }).then(function () {
                                    window.location.href = PATH + '/produto'
                                })
                            }
                        });
                    }else{
                        $.ajax({
                            url: PATH + 'produto/salvar_produto/',
                            data: formData,
                            type: 'POST',
                            dataType: 'json',
                            mimeType: "multipart/form-data",
                            contentType: false,
                            cache: false,
                            processData: false,
                            async: false,
                        }).done(function(res) {

                            array_res = res[0];
                            if(typeof res[0].erro != "undefined"){
                                Swal.fire({
                                    icon: 'error',
                                    text: res[0].erro,
                                    confirmButtonText: "Continuar",
                                    confirmButtonColor: "#ffc107"
                                }).then(function () {
                                    return false;
                                })
                            } else {
                                Swal.fire({
                                    icon: 'success',
                                    text: 'Produto cadastrado com sucesso',
                                    confirmButtonText: "Continuar",
                                    confirmButtonColor: "#ffc107"
                                }).then(function () {
                                    window.location.href = PATH + '/produto'
                                })
                            }
                        });
                    }
                    e.preventDefault();

                    return true;

                });

                $('#product-form').submit();
            
                
            }
        })
    }

    $(document).ready(function () {
        $('#name').focus()
        masks();
        save();
        clickphoto();
    });

})($, PATH, Helpers);