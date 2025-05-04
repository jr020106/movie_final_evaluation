from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path('ComingSoon/', views.ComingSoon, name='ComingSoon'),
    path('topMovies/', views.topMovies, name='topMovies'),
    path('login/', views.login, name='login'),
    path('moviedetail/<slug:movie_slug>/', views.moviedetail, name='moviedetail'),
    path('arrival/', views.arrival, name='arrival'),
    path('interstellar/', views.interstellar, name='interstellar'),
    path('johnwick/', views.johnwick, name='johnwick'),
    path('jurassicpark/', views.jurassicpark, name='jurassicpark'),
    path('kalki/', views.kalki, name='kalki'),
    path('madmax/', views.madmax, name='madmax'),
    path('missionimpossible/', views.missionimpossible, name='missionimpossible'),
    path('martian/', views.martian, name='martian'),
    path('maverick/', views.maverick, name='maverick'),
    path('spacejam/', views.spacejam, name='spacejam'),
    path('thematrixrevolutions/', views.thematrixrevolutions, name='thematrixrevolutions'),
    path('war/', views.war, name='war'),
    path('yodha/', views.yodha, name='yodha'),
    path('MovieFlix/', views.MovieFlix, name='MovieFlix'),
    path('review/', views.review, name='review'),
    path('reveiw/', views.reveiw, name='reveiw'),
]

