from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse('Hello world !')


def home_page_view_with_render(request):
    return render(request, "index.html")

def sign_up_page(request):
    if request.method == "POST":
        print(request.POST)
        alpha = request.POST["data"]
        print(alpha)
    return render(request, "inscription.html",{"value1":"Valeur envoyé depuis views.py"})