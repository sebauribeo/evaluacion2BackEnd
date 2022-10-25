from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vista1', views.vista1, name='vista1'),
    path('vista2', views.vista2, name='vista2'),
    path('vista3', views.vista3, name='vista3'),
    path('vista4', views.vista4, name='vista4'),
]