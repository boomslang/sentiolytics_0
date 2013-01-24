from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.db import connection
from django.utils import simplejson

def test(request):
    return render_to_response('main/test.html')

def ajax_load_view(request,view_name):
    if not request.is_ajax():
        raise Http404
    return render_to_response("main/views/"+ view_name + "_view.html")


def ajax_load_mw_tab(request,tab_name):
    if not request.is_ajax():
        raise Http404
    return render_to_response("main/views/mw_tabs/"+ tab_name + ".html")

def ajax_load_leagues(request):
    if not request.is_ajax():
        raise Http404

    return HttpResponse(simplejson.dumps(load_leagues()), mimetype='application/json')

def load_leagues():
    sql_string = "SELECT LEAGUE_ID, LEAGUE_NAME FROM sentiosp_drupal6.td_league;"
    cursor = connection.cursor()
    cursor.execute(sql_string)
    data = cursor.fetchall()
    #    data_list = list({id: x, name: y} for x, y in data)
    return data

def ajax_load_matches(request):
    if not request.is_ajax():
        raise Http404

    league_id = request.GET.get('sendValue')

    sql_string = "SELECT MATCH_ID, HOME_TEAM_ID, VISITOR_TEAM_ID FROM sentiosp_drupal6.tf_match WHERE MATCH_LEAGUE_ID =" + league_id + ";"
    cursor = connection.cursor()
    cursor.execute(sql_string)
    matches = cursor.fetchall()

    home_team_ids = list(match[1] for match in matches)
    away_team_ids = list(match[2] for match in matches)
    team_ids = list(set(home_team_ids + away_team_ids))

    sql_string = "SELECT TEAM_ID, TEAM_NAME FROM sentiosp_drupal6.td_team WHERE "

    for team_id in team_ids:
        sql_string += " TEAM_ID = " + str(team_id) + " OR"

    sql_string += " FALSE"
    cursor = connection.cursor()
    cursor.execute(sql_string)
    returned_data = cursor.fetchall()
    team_names = dict(returned_data)

    data = list()

    for match in matches:
        try:
            data.append((match[0], team_names[match[1]], team_names[match[2]] ))
        except:
            print match
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')
