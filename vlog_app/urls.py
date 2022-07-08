from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('post-detail/<int:post_id>/', post_detail, name="post-detail"),
    path('sing_up', registration, name="sing-up"),
    path('edit-post/<int:post_id>/', edit_post, name='edit-post'),
    path('create-post/', create_post, name="create-post"),
    
]
