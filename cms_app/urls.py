from django.urls import path
from . import views

urlpatterns = [
    path('create', views.Blog.as_view({'post': 'create'}), name="blog"),
    path('list', views.Blog.as_view({'get': 'list'}), name="blog")
]
