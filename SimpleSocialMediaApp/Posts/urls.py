# POSTS APP URL.PY FILE
from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('new/', views.CreatePost.as_view(), name='create_post'),
    path('by/<str:username>', views.UserPosts.as_view(), name='user_post_list'),
    path('by/<str:username>/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='post_delete'),
]
