from django.urls import path
from . import views

urlpatterns = [
    path('home', views.storehome , name='home'),
    path('funding', views.aboutus , name ='funding'),

]
