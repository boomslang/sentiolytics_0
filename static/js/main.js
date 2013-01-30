$(document).ready(function(){

    $('#matches_button').click(function()    {
        load_view("match_select","match_select");
    });
    $('#teams_button').click(function()    {
        load_view("team_select","team_select");
    });
    $('#players_button').click(function()    {
        load_view("player_select","player_select");
    });

//    load_script("match_select");
//    load_script("match");
});

//function add_to_session()
//{
//    if(arguments.length == 1)
//    {
//        $.get('ajax_add_to_session',arguments[0])
//    }
//    else if(arguments.length == 2)
//    {
//        $.get('ajax_add_to_session',arguments[0])
//            .done(function() {
//                arguments[1];
//            })
//
//    }
//}

function request_load_leagues(prefix)
{
    $.ajax({
        url: '/ajax_load_leagues/',
        type: 'GET',
        data: {sendValue:'test'},
        success: function(data){
            load_leagues(data,prefix)
        },
        dataType: 'json'
    });
}

function load_leagues(data,prefix)
{
    var select_name = "#" + prefix + "_select_league";
    var option_name = "#" + prefix + "_league_option";
    $(select_name).empty()
        .append(
        $('<option>')
            .append('Select a league')
        );

    for(var i = 0; i < data.length; i++)
    {
        $(select_name)
            .append(
            $('<option>')
                .attr("class", option_name)// with given name
                .attr("league_id", data[i][0])
                .append(data[i][1])
            )
    }
    $(select_name).change(function () {
        $(select_name +" option:selected").each(function () { // TODO: (murat) $(this).find(":selected").
            var league_id = $(this).attr('league_id');
            if(league_id != undefined )
            {
                request_load_matches(league_id, prefix);
//                alert($(this).attr('league_id'))
            }
        });
    })

}

function request_load_matches(data_to_send, prefix)
{
    $.ajax({
        url: '/ajax_load_matches/',
        type: 'GET',
        data: {sendValue : data_to_send},
        success: function(data){
            fill_select_match(data,prefix)
        },
        dataType: 'json'
    });
}


function fill_select_match(data,prefix)
{
    var select_name = "#" + prefix + "_select_match";
    var option_name = "#" + prefix + "_match_option";
    $(select_name).empty()
        .append(
        $('<option>')
            .append('Select a match')
    );
    for(var i = 0; i < data.length; i++)
    {
        $(select_name)
            .append(
            $('<option>')
                .attr("class", option_name)// with given name
                .attr("match_id", data[i][0])
                .attr("teams", data[i][1] + " - " + data[i][2])
                .append(data[i][1] + " - " + data[i][2])
        )
    }
}
function load_view()
{
    $("#page").empty();

    if(arguments.length == 1)
    {
    //    $("#page").load("/ajax_load_" + view_name +"/", load_script(view_name))
        $("#page").load("/ajax_load_" + arguments[0] +"/")
            .css('visibility','visible');
    }
    else if(arguments.length == 2)
    {
        var script_name = arguments[1];
        $.get("/ajax_load_" + arguments[0] +"/", function(data) {
            $("#page").html(data);
        })
            .done(function() {
                load_script(script_name);
//                alert(script_name);
            })
    }

}


function load_script(view_name)
{
    $.getScript(STATIC_URL + 'js/' + view_name + '.js');
}