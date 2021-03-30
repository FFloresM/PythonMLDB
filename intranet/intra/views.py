from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    var = "hola mundo"
    return render(request, "intra/base.html", {"hola": var})
    