from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect # This is our responses
from django.urls import reverse
from .models import Dog
from django.contrib.auth.models import User

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    # def get(self, request):
    #     return HttpResponse("Dogs Home")

class About(TemplateView):
    template_name = 'about.html'

    # def get(self, request):
    #     return HttpResponse("Dogs About")
# class Dog:
#     def __init__(self, name, age, gender, breed):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.breed = breed

class Dog_List(TemplateView):
    template_name = 'doglist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #this gets the name query parameter to access it 
        name = self.request.GET.get("name")
        #if the query exists we will filter by name
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["dogs"] = Dog.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else: 
            context['dogs'] = Dog.objects.all() # this is where we add the key into our context object for the view to use
            context['header'] = "Our Dogs"
        return context

class Dog_Create(CreateView):
    model = Dog
    fields = ['name', 'img', 'age', 'gender', 'breed', 'user']
    template_name = "dog_create.html"
    # def get_success_url(self):
    #     return reverse('dog_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/dogs')

class Dog_Detail(DetailView):
    model = Dog
    template_name="dog_detail.html"

class Dog_Update(UpdateView):
    model = Dog
    fields = ['name', 'img', 'age', 'gender', 'breed']
    template_name = "dog_update.html"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

class Dog_Delete(DeleteView):
    model = Dog
    template_name = "dog_delete_confirmation.html"
    success_url = "/dogs/"

#user profile
def profile(request, username):
    user = User.objects.get(username=username)
    dogs = Dog.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'dogs': dogs})