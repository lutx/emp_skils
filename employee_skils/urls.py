"""employee_skils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from . import settings
from emp_app import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from jet_django.urls import jet_urls
from jet.dashboard.dashboard_modules import google_analytics_views

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet_api/', include(jet_urls)),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url('admin/', admin.site.urls),
    url('', include('emp_app.urls'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
