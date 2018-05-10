$(document).ready(function () {
    /*$('.dropdown').dropdown();*/
    $('.vinculo').change(function () {
        $('.vinculo option:selected').each(function () {

            var selecionado = $(this).text();
            if (selecionado.trim() == "Professor") {
                $('.matricula').text('')
                $('.matricula').text('SIAPE')
                $('.periodo').hide()
                $('.curso').hide()
                $('.tres').removeClass('three').removeClass('fields')
            }
            else {
                $('.matricula').text('')
                $('.matricula').text('Matrícula')
                $('.periodo').show()
                $('.curso').show()
                $('.tres').addClass('three').addClass('fields')
            }
        })


    })

    $('.ui.accordion').accordion();

    $('.ui.checkbox')
        .checkbox()
    ;

    $('.atividade .field input').each(function () {
        if ($(this).attr('id') == 'id_nome')
            conteudo = $(this).val()
        if (conteudo != '')
            $('.direita').css('margin-top', '-30px');
    })

    $('.special.cards .image').dimmer({
        on: 'hover'
    });

    $('.your.element')
        .sidebar('behavior name', argumentOne, argumentTwo)
    ;

    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade')
            ;
        })
    ;
})
