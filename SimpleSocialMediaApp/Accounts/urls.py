from django.urls import path
from django.contrib.auth import views as auth_views
from Accounts import views

app_name = 'Accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Accounts\login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), kwargs={'next_page':''}, name='logout'),
    path('signup/', views.User_Registration.as_view(), name='signup')
]
