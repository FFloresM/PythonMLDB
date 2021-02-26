from django.http import HttpResponse


def index(request):
    return HttpResponse("Mi primera app Intranet")
    