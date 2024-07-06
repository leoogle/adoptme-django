"""
URL configuration for adoptme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls: import: path, include
from adoptme import views
from client_app import views as client_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin_app/', include('admin_app.urls', namespace='admin_app')),
    path('client_app/', include('client_app.urls', namespace='client_app')),
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    path('donaciones/', views.donaciones, name='donaciones'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', client_views.registro, name='registro (client_apps)'),
    path('iniciar_sesion/', client_views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', client_views.cerrar_sesion, name='cerrar_sesion'),
]
