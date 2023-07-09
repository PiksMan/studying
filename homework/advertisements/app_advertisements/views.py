from django.shortcuts import render
from django.http import HttpResponse

#обработка запроса
def index(request):
    return HttpResponse("Успешно!")

# Create your views here.
