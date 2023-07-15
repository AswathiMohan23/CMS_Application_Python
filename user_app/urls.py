from django.urls import path
from . import views

urlpatterns = [
    path('register', views.UserRegistration.as_view({'post': 'create'}), name="register"),
    path('login', views.UserLogin.as_view({'post': 'create'}), name="login"),
]

