from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango Says hey there partner")

def about(request):
    return HttpResponse("Rango Says here is the about page")

