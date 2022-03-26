from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='indexd'),
    path('signu',views.signup,name='signupd'),
    path('signi',views.signin,name='signind'),
    path('signo',views.signout,name='signoutd'),
    path('fileu',views.fileread,name='filereadd'),
    path('article/',views.ticketlist),
    path('detail/<str:input1>/',views.ticketdetail),
    path('article2/',views.ticket_responselist),
    path('detail2/<str:input1>/',views.ticket_responsedetail),
]