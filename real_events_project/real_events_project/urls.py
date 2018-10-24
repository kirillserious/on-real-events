"""real_events_project URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include

from real_events_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    path('', views.index, name='index'),
    path('places/', views.all_places, name='all_places'),
    path('news/', views.all_news, name='all_news'),
    path('meetings/', views.all_meetings, name='all_meetings'),
    path('referees/', views.all_referees, name='all_referees'),
    path('staff/', views.all_staff, name='all_staff'),
    path('members/', views.all_members, name='all_members'),
    path('teams/', views.all_teams, name='all_teams'),
    re_path(r'^places/(?P<place_slug>[\w\-]+)/$', views.place, name='place'),
    re_path(r'^news/(?P<news_post_slug>[\w\-]+)/$', views.news_post, name='news_post'),
    re_path(r'^meetings/(?P<meeting_slug>[\w\-]+)/$', views.meeting, name='meeting'),
    re_path(r'^referees/(?P<referee_slug>[\w\-]+)/$', views.referee, name='referee'),
    re_path(r'^staff/(?P<staff_slug>[\w\-]+)/$', views.staff, name='staff'),
    re_path(r'^members/(?P<member_slug>[\w\-]+)/$', views.member, name='member'),
    re_path(r'^teams/(?P<team_slug>[\w\-]+)/$', views.team, name='team'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
