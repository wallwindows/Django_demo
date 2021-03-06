"""Django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from demo_form.views import form_view
from demo_paginator.views import paginator_view
from demo_session.views import login_view, index_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # demo_form
    path('forms/', form_view, name='forms'),
    # demo_paginator
    path('paginator/', paginator_view, name='paginator'),
    # demo_session
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('logout/', logout_view, name='index'),

]
