from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.Blog.as_view({'post': 'create'}), name="blog")
]
