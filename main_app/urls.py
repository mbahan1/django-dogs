from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"), # <- here we have added the new path
	path('dogs/', views.DogList.as_view(), name="dog-list"),

]