$(document).ready(function(){

    $('#matches_button').click(function()    {
        clear_page();
//        alert('t')
        load_view("match_select");
    });

    load_script("match_select");
    load_script("match");

});


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
//        $.getScript(STATIC_URL + 'js/match_select.js');
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