from django.shortcuts import render

def index(request):
    var = "hola mundo"
    return render(request, "intra/base.html", {"hola": var})
    