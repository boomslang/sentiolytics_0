$(document).ready(function(){
    $('#matches_button').click(function()    {
        load_view("match_select");
    });
});


function load_view(view_name)
{
    $("#page").load("/ajax_load_" + view_name +"/", load_scripts(view_name))
//    $("#page").load("/ajax_load_match_select/", load_scripts(view_name))
            .css('visibility','visible');

}

function load_scripts(view_name)
{
//    alert('t')
    if(view_name == "match_select")
    {
        $.getScript(STATIC_URL + 'js/match_select.js');
    }
    else if(view_name == "match")
    {
        $.getScript(STATIC_URL + 'js/match_view.js');
    }

}



function clear_page()
{
    $("#page").empty()
        .css('visibility', 'hidden'); // TODO : Sonradan unutma. (Murat)
}