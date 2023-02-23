from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path("",views.posts, name="posts"),
    path("add-post/",views.addPost, name="add-post"),
]