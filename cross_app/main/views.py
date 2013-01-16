from django.http import Http404
from django.shortcuts import render_to_response

def test(request):
    return render_to_response('main/test.html')

def load_view(request,view_name):   # TODO: murat - url parametre okuma sorununu cozunce buna gec.
    if not request.is_ajax():
        raise Http404
    return render_to_response("main/views/"+ view_name + "_view.html")