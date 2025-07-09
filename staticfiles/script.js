$(document).ready(function(){

        $('#add-lista').click(function(){
            $('.container').slideDown();
        })
        $('.resume').click(function(){
            $('.container').slideUp();
            $('ul').empty();
        })

        $('form').on('submit', function(e){
            e.preventDefault();

            const novaTarefa =$('#input-add-tarefa').val();
            const addNovaTarefa =$('<li></li>').append(
                `<input type="checkbox" class="tarefa" id="${novaTarefa}">
                <label for="${novaTarefa}" id="label-tarefa">${novaTarefa}</label>`
            )

            $('ul').append(addNovaTarefa);
            $('#input-add-tarefa').val('');
            
        });

        $('ul').on('change', '.tarefa', function(){
            const label = $(this).next('label');
            if ($(this).prop('checked')) {
                label.css('text-decoration', 'line-through');
            } else {
                label.css('text-decoration', 'none');
            }
        });

        
});


