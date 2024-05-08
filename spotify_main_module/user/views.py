from . import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def create_user(user):
    return models.create_user(user)
