from django.http import HttpResponse
from . import artist


def index(request, message=artist.Artist.test(artist.Artist()), content_type="application/json"):
    return HttpResponse(message, content_type=content_type)
