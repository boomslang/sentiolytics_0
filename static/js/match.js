$(document).ready(function(){
//    loadPlayers();
//    fillDrawChart([]);

//    alert('$')
    $('#page').on('click', '#mw_tab a', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
//    $('#page').on('ready', '#mw_tab', function (e) {
//        alert('asd')
//    });
    $('#mw_tab').ready(function() {
        load_mw_tabs();
    });

    req_load_mw_score();
//    $('#Slider1').slider().onstatechange(function(){
//        update_chart();
//    });


});

function req_load_mw_score()
{
    $.get('ajax_mw_load_score',function(data) {load_mw_score(data)},'json');
//    $.ajax({                                                      // Works just fine as .get() - Murat
//        url: 'ajax_mw_load_score',
//        type: 'GET',
////        data: {sendValue:data_to_send},
//        success: function(data){
//            load_mw_score(data)
//        },
//        dataType: 'json'
//    });
}

function load_mw_score(data)
{
    var teams = data[0].split(' - ');

    $('.mw_team_1').empty()
        .append(teams[0]);
    $('.mw_team_2').empty()
        .append(teams[1]);
    $('.mw_score').empty()
        .append(data[1]);
}

function load_mw_tabs()
{
    $('#mw_tab_summary').empty()
        .load('ajax_load_mw_tab_summary');
    $('#mw_tab_chalkboard').empty()
        .load('ajax_load_mw_tab_chalkboard');
    $('#mw_tab_radar').empty()
        .load('ajax_load_mw_tab_radar');
    $('#mw_tab_performance').empty()
        .load('ajax_load_mw_tab_performance');
}

// Load the Visualization API and the piechart package.
google.load('visualization', '1.0', {'packages':['corechart']});

//// Set a callback to run when the Google Visualization API is loaded.
//google.setOnLoadCallback(drawChart);



function fillDrawChart(returned_data) {
    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Player');
    data.addColumn('number', 'Distance');


    data.addRows(returned_data);
    // Set chart options
    var options = {'title':'Distance',
        'width':400,
        'height':300};

// Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}
function loadPlayers(){ // TODO: Checkbox bilgilerini doldur
    $.get("/load_players/",{ /*sendValue: str*/ },
        function(data){
            for(var j = 0; j < 2; j++)
            {
                for(var i = 0; i < data[j].length; i++)
                {
                    $("#players_team"+(j+1))
                        .append(
                        $("<input/>")
                            .attr("type", "checkbox")//of type checkbox
                            .attr("class", "player_cb"+(j+1))// with given name
                            .attr("checked", false)// checked="checked" or checked=""
                            .attr("name", "player")
                            .attr("team", data[2][j]) // TODO: Team id'leri gonderilen array'e [2] olarak ekle. checkbox'lara attr olarak eklemeye calis
                            .attr("value", data[j][i][1])
                    )
                        .append('<label> ' + data[j][i][0] + '</label><br>');
                }

                $('.player_cb'+(j+1)).click(function()    {
                    update_chart();
                });
            }
            $('.check_all').click(
                function()
                {
                    $("INPUT[class='player_" + $(this).attr('id') + "']").attr('checked', $(this).is(':checked'));
                    update_chart()
                }
            );
        }, "json");
}
function update_chart(){
    var data_to_send = [];

    data_to_send.push($("#Slider1").slider('value'));

//    $('.player_checkbox').each(function(i, obj) {
//        if( obj.is(':checked') == true )
//        {
//            alert(player_ids);
//            player_ids.push($('this').attr('name'));
//        }
//    });
    $('input[name="player"]:checked').each(function(){
        data_to_send.push($(this).attr('team') + '-' + $(this).attr('value') );
    });

    $.ajax({
        url: '/ajax_update_chart/',
        type: 'GET',
        data: {sendValue:data_to_send},
        success: function(data){
            fillDrawChart(data)
        },
        dataType: 'json'
    });
}
