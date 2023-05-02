"""gardenplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dashboard import views as dashboard_views
from gardenbed import views as gardenbed_views
from journal import views as journal_views
from forum import views as forum_views
from plantlog import views as plantlog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.dashboard),
    path('gardenbed/', gardenbed_views.gardenbed),
    path('gardenbed/add/', gardenbed_views.add),
    path('gardenbed/edit/<int:id>/', gardenbed_views.edit),
    path('gardenbed/entry/<int:id>/', gardenbed_views.entry),
    path('plantlog/', plantlog_views.plantlog),
    path('plantlog/add/', plantlog_views.add),
    path('plantlog/edit/<int:id>/', plantlog_views.edit),
    path('plantlog/entry/<int:id>/', plantlog_views.entry),
    path('journal/', journal_views.journal),
    path('journal/add/', journal_views.add),
    path('journal/edit/<int:id>/', journal_views.edit),
    path('journal/entry/<int:id>/', journal_views.entry),
    path('login/', dashboard_views.user_login, name='user_login'),
    path('logout/', dashboard_views.user_logout, name='user_logout'),
    path('join/', dashboard_views.join, name='join'),
]
