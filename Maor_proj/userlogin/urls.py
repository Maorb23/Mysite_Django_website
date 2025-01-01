from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import test_messages
from django.urls import include


app_name = 'Maor_proj.userlogin'

urlpatterns = [
    #path('login_user', views.login_user, name='login'),
    #path('', views.main_index, name='main_index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # Add other URLs as needed
]  

