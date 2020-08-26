from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('signin', views.signin, name = 'signin'),
    path('register', views.register, name = 'register'),
    path('enter', views.enter, name = 'enter'),
    path('home', views.home, name = 'home'),
    path('logout', views.logout, name = 'logout')

]