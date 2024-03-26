from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Salom siz saytga xush kelibsiz")