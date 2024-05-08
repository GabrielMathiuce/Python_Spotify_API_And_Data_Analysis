import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import artist


@csrf_exempt
def index(request, message=artist.Artist.test(artist.Artist()), content_type="application/json"):
    response = HttpResponse(json.dumps({'response': request.method}), content_type=content_type)
    response.status_code = 403
    return response
    #return HttpResponse(message, content_type=content_type)


def favorite(request, message=artist.Artist.test(artist.Artist()), content_type="application/json"):
    return HttpResponse(json.dumps({'response': 'Mac DeMarco is your favorite artist'}), content_type=content_type)