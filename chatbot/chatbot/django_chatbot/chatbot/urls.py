from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    # path('', views.chatbot, name='chatbot'),

    # menu
    path('chatbot', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

    # routing
    path('', views.landing_page, name='index'),

    # courses: user dashboard
    path('hr', views.hr, name='hr'),
    path('excel', views.excel, name='excel'),
    path('infotech', views.infotech, name='infotech'),

    # video/speech    
    path('video', views.video, name='video'),
    path('speechtext', views.speechtext, name='speechtext'),
 
    # Poll/Questionnaire
    path('create', views.create, name='create'),
    path('pollhome', views.pollhome, name='pollhome'),
    path('pollresult/<int:poll_id>/', views.pollresult, name='pollresult'),
    path('pollvote/<int:poll_id>/', views.pollvote, name='pollvote'),
    path('pollresult_success', views.pollvote, name='pollresult_success'),

    # FROM: POLL ONLY
    # path('base', views.results, name='result\s'),
    # path('create', views.create, name='create'),
    # path('home', views.home, name='home'),
    # path('results', views.results, name='results'),
    # path('vote', views.vote, name='vote'),

    # path('chatbot/', views.members, name='members'),
    # path('chatbot/details/<int:id>', views.details, name='details'),
]

    
