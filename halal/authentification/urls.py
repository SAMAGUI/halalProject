from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name="index"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerPage, name="register"),
]