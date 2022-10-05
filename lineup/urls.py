from django.urls import path
from lineup import views

urlpatterns = [
    path('', views.hello_world, name='hello')
]