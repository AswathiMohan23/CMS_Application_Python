from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.Blog.as_view({'post': 'create','get': 'list'}), name="blog"),
    path('blog/<int:blog_id>', views.Blog.as_view({'put': 'update','delete':'destroy'}), name="blog"),
]
