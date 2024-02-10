from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path("<int:postID>/blog", views.blogpost, name="blogpost"),
    path("blog", views.blogHome, name="blogHome")

]