# Maor_proj.cv/urls.py

from django.urls import path
from Maor_proj.cv import views

app_name = 'Maor_proj.cv'

urlpatterns = [
    path('', views.cv_view, name='cv_view'),
    path('download/<int:cv_id>/', views.download_cv, name='download_cv'),
    path('test/', views.test_view, name='test_view'),
    path('success/', views.cv_success, name='cv_success'),
]
