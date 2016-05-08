from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..forms import GminaEditForm

@login_required(login_url='login')
def edit_gmina(request):
    if request.method == 'POST':
        form = GminaEditForm(data = request.POST)
    else:
        form = GminaEditForm(gminaid=int(request.GET['gid']))
    return render(request, 'edit.html', { 'form' : form })
