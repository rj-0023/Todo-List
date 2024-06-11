"""
URL configuration for Todo_list project.

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
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('data/', views.dataview, name="Data"),
    path('data/<int:id>', views.dynamicview, name="Dynamic"),
    path('data/delete/<int:id>', views.deleteview, name="deleteview"),
    path('data/edit/<int:id>', views.updateview, name="editview"),
    path('form/', views.formview, name="Form"),
    path('accounts/login/',views.login_user, name="login"),
    path('accounts/logout/',views.logout_user, name="logout"),

    path('register/',views.register_user, name="register_user"),


]
