$(document).ready(function(){

    $('#matches_button').click(function()    {
        clear_page();
//        alert('t')
        load_view("match_select");
        request_load_leagues();
    });

    load_script("match_select");
    load_script("match");
});

function request_load_leagues()
{
    $.ajax({
        url: '/ajax_load_leagues/',
        type: 'GET',
        data: {sendValue:'test'},
        success: function(data){
            load_leagues(data)
        },
        dataType: 'json'
    });
}

function load_leagues(data)
{
    $("#msw_select_league").empty();
    for(var i = 0; i < data.length; i++)
    {
        $("#msw_select_league")
            .append(
            $('<option>')
                .attr("class", "msw_league_option")// with given name
                .attr("league_id", data[i][0])
                .append(data[i][1])
            )
    }
    $("#msw_select_league").change(function () {
        $("#msw_select_league option:selected").each(function () {
            alert($(this).attr('league_id'))
    });
})

}

function load_view(view_name)
{

//    $("#page").load("/ajax_load_" + view_name +"/", load_script(view_name))
    $("#page").load("/ajax_load_" + view_name +"/")
        .css('visibility','visible');

}

function load_script(view_name)
{
//    alert('t');
    $.getScript(STATIC_URL + 'js/' + view_name + '.js');
//    if(view_name == "match_select")
//    {
//        $('#page').on('click', '#match_select_button', function () {
////    $("#match_select_button").click(function()    {
//            load_view("match");
//            alert('ahoy2');
//        });
////    clear_page();
//        $('#page').on('change', '#msw_select_league', function () {
//            $("select option:selected").each(function () {
//                alert($(this).text())
//            });
//        });
//
//
//    }
//    else if(view_name == "match")
//    {
//        $.getScript(STATIC_URL + 'js/match.js');
//    }

}

function clear_page()
{
//    var node = $("#page");
//    while (node.hasChildNodes()) {
//        node.removeChild(node.lastChild);
//    }
    $("#page").empty();
//        .css('visibility', 'hidden'); // TODO : Sonradan unutma. (Murat)
}