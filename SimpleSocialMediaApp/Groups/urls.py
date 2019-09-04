# GROUPS APP URL.PY FILE

from django.urls import path
from . import views

app_name = 'Groups'

urlpatterns = [
    path('create/', CreateGroup.as_view(), name='create_group'),
    path('posts/in/<slug>/', GroupDetail.as_view(), name='group_detail'),
    path('', GroupList.as_view(), name='group_list'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),
]
