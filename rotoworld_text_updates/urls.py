"""rotoworld_text_updates URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

import settings
from data.views import TeamViewSet, PositionViewSet, SportViewSet, LeagueViewSet, PlayerNewsViewSet, PlayerViewSet
from users.views import UserCreate, UserUnsubscribe, signup, thanks, unsubscribe, goodbye, UserDestroyView

team_list = TeamViewSet.as_view({
    'get': 'list'
})

team_detail = TeamViewSet.as_view({
    'get': 'retrieve'
})

position_list = PositionViewSet.as_view({
    'get': 'list'
})

position_detail = PositionViewSet.as_view({
    'get': 'retrieve'
})

player_list = PlayerViewSet.as_view({
    'get': 'list',
})
player_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
})

sport_list = SportViewSet.as_view({
    'get': 'list'
})

sport_detail = SportViewSet.as_view({
    'get': 'retrieve'
})

league_list = LeagueViewSet.as_view({
    'get': 'list'
})

league_detail = LeagueViewSet.as_view({
    'get': 'retrieve'
})

player_news_list = PlayerNewsViewSet.as_view({
    'get': 'list'
})

player_news_detail = PlayerNewsViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^goodbye/$', goodbye, name='goodbye'),
    url(r'^unsubscribe/$', unsubscribe, name='unsubscribe'),
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^add_user/$', UserCreate.as_view(), name='user-add'),
    url(r'^delete_user/$', UserDestroyView.as_view(success_url="http://rotoworld-updates.herokuapp.com/goodbye/"), name='user-delete'),
    url(r'^players/$', player_list, name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', player_detail, name='player-detail'),
    url(r'^teams/$', team_list, name='team-list'),
    url(r'^teams/(?P<pk>[0-9]+)/$', team_detail, name='team-detail'),
    url(r'^positions/$', position_list, name='position-list'),
    url(r'^positions/(?P<pk>[0-9]+)/$', position_detail, name='position-detail'),
    url(r'^sports/$', sport_list, name='sport-list'),
    url(r'^sports/(?P<pk>[0-9]+)/$', sport_detail, name='sport-detail'),
    url(r'^leagues/$', league_list, name='league-list'),
    url(r'^leagues/(?P<pk>[0-9]+)/$', league_detail, name='league-detail'),
    url(r'^player_news/$', player_news_list, name='player_news-list'),
    url(r'^player_news/(?P<pk>[0-9]+)/$', player_news_detail, name='player_news-detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
