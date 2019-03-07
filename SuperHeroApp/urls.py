from django.urls import path
from . import views

urlpatterns = [
    path('welcome/index/', views.index, name='index'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('welcome/', views.welcome, name='welcome'),


]