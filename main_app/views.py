from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse # This is our responses

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    # def get(self, request):
    #     return HttpResponse("Dogs Home")

class About(TemplateView):
    template_name = 'about.html'

    # def get(self, request):
    #     return HttpResponse("Dogs About")
class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

dogs = [
    Dog("Mau", 5, "Female"),
    Dog("Garfield", 43, "Male"),
    Dog("Meowth", 25, "Male"),
    Dog("Salem", 500, "Male"),
]

class DogList(TemplateView):
    template_name = 'doglist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dogs"] = dogs # this is where we add the key into our context object for the view to use
        return context