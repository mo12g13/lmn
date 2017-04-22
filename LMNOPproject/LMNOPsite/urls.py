"""LMNOPsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from LMNOPproject.lmn import views, views_users
from django.conf import settings
from LMNOPproject.lmn import views_social as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),    #Admin site

    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', views_users.logout_view, name='logout'),
    url(r'^register/$', views_users.register, name='register'),

    url(r'^', include('LMNOPproject.lmn.urls') ),

    #login with social media
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
