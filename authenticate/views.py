import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def sign_up(request):
    return HttpResponse('<h1> Inscription </h1>')

def log_in(request):
    return HttpResponse('<h1> Connexion </h1>')

def log_out(request):
    return HttpResponse('<h1> Deconnexion </h1>')
