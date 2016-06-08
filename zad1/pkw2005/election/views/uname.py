from jsonview.decorators import json_view

@json_view
def currentUser(request):
    if(not request.user.is_authenticated()):
        return { "id": None }
    else:
        return { "id"       : request.user.id,
                 "username" : request.user.get_username()
                 }

