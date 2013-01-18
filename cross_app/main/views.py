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