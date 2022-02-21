from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='indexd'),
    path('signu',views.signup,name='signupd'),
    path('signi',views.signin,name='signind'),
    path('signo',views.signout,name='signoutd'),
]