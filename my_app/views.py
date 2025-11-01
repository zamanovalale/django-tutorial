from django.http import HttpResponse

def index(request):
    return HttpResponse("Salam, Django işlədi!")
