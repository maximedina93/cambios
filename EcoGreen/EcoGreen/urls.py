"""EcoGreen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.EcoGreen, name='EcoGreen')
Class-based views
    1. Add an import:  from other_app.views import EcoGreen
    2. Add a URL to urlpatterns:  path('', EcoGreen.as_view(), name='EcoGreen')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.EcoGreen, name = 'EcoGreen'),
    
    path('login/', auth.LoginView.as_view(template_name="usuarios/login.html"), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),


    #PATH QUE APUNTAN A APPS
    path('post/', include('apps.post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

