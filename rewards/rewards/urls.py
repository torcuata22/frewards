"""rewards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include ('rewards.urls')),
    path('', views.home, name="home"),
    path('rewards', views.all_points, name='all-points'),
    path('dannon', views.d_payer_points, name='d-points'),
    path('miller', views.m_payer_points, name='m-points'),
    path('unilever', views.u_payer_points, name='u-points'),
    path('spend_points', views.spend_points, name='spend-points'),
    path('update', views.flatten_updated_records, name = 'update-records')
   
]
