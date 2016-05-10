from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.request import QueryDict 
from jsonview.decorators import json_view
from ..forms import GminaEditForm
from ..models import Gmina

@login_required(login_url='login')
def edit_gmina(request):
    if request.method == 'POST':
        print(str(request.POST))
        form = GminaEditForm(data = request.POST)
    else:
        form = GminaEditForm(gminaid=int(request.GET['gid']))
    return render(request, 'edit.html', { 'form' : form })

@login_required(login_url=None)
@json_view
def submit_gmina(request):
    if request.method == "GET":
        return {'ok': False}
    else:
        form = GminaEditForm(data = request.POST)
        if form.is_valid():
            gm = Gmina.objects.get(id = form.cleaned_data.get("gid"))
            if request.POST['try'] == "n":
                st = gm.update_glosy(form.cleaned_data.get("k1"),
                        form.cleaned_data.get("k2"),
                        form.cleaned_data.get("rev"),
                        request.user)
            else:
                st = True
            if gm.revuser is not None:
                uname = gm.revuser.username
            else:
                uname = "admin"
            return {'ok'      : st,
                    'revtime' : gm.revtime.strftime("%H:%M %d.%m.%Y"),
                    'revuser' : uname}
        else:
            return {'ok': False}
