$(document).ready(function(){
    request_load_leagues();
//    $('#page').on('click', '#match_select_button', function () {
    $("#match_select_button").click(function()    {
        $.get('ajax_add_to_session',{
            match_id : $('#msw_select_match').find(":selected").attr('match_id'),
            teams : $('#msw_select_match').find(":selected").attr('teams')
        })
            .done (function () {
                load_view('match','match');
        });


//        alert('ahoy2');

//         $('#msw_select_match').find(":selected").attr('match_id')

    });
//    clear_page();
//    $('#page').on('change', '#msw_select_league', function () {
//        $("select option:selected").each(function () {
//            alert($(this).attr('league_id'))
//        });
//    });
//    alert('test2');
});