"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Maor_proj.userlogin import views
from Maor_proj.userlogin.views import test_messages

from . import views2

urlpatterns = [
    path('', views2.main_index, name='main_index'),  # The index view
    path('<int:year>/<str:month>', views2.main_index, name='main_index'),
    path('cv/', include('Maor_proj.cv.urls', namespace='Maor_proj.cv')),
    path('articles/', include('Maor_proj.articles.urls', namespace='Maor_proj.articles')),
    path('polls/', include('Maor_proj.polls.urls')),  # Include the polls URLs
    path('admin/', admin.site.urls),
    path('userlogin/', include('Maor_proj.userlogin.urls', namespace='Maor_proj.userlogin')),
    path('userlogin/', include('django.contrib.auth.urls')),
    path('birthday/', include('Maor_proj.birthday_problem.urls', namespace='Maor_proj.birthday_problem')),
    path('test/', test_messages, name='test_messages'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
