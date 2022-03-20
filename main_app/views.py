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
    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

dogs = [
    Dog("Loki", 8, "Male", "GSD mutt"),
    Dog("Han Solo", 8, "Male", "Idaho Fuzzy"),
    Dog("Titus", 14, "Male", "Australian Shepard"),
    Dog("Zephyr", 4, "Male", "Border Collie mutt"),
    Dog("Zoe", 14, "Female", "Labrador Retriever"),
    Dog("Penny", 9, "Female", "Lab/GSD mutt"),
]

class DogList(TemplateView):
    template_name = 'doglist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dogs"] = dogs # this is where we add the key into our context object for the view to use
        return context