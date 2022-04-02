from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api', views.Get, name="Get"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
