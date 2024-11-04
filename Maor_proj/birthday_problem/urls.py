from django.urls import path
from . import views

app_name = 'Maor_proj.birthday_problem'

urlpatterns = [
    path('', views.birthday_problem_view, name='birthday_template'),
]