from django.contrib.auth.models import User
import pdb

from django.http import HttpResponse
import json


def create_user(self):
    pdb.set_trace()
    user = UserModel.objects.create_user(username='lonelyfeeling', email='gabriel.mathiuce@ibm.com', password='verystrongpassword')
    user.first_name('Gabriel')
    user.last_name('Mathiuce')
    user.save()
    response = HttpResponse("User: " + json.dumps({
        'Username': user.username,
        'Email': user.email,
        'Password': user.password,
        'First Name': user.first_name,
        'Last Name': user.last_name,
    }) + "created with success")
    response.status_code = 201
    return response


class UserModel(User):
    pass




    
    
   



