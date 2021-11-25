from django import views
from django.urls import path
from django.urls import path
from .views import LoginView, UserView


urlpatterns=[
    path('users/',UserView.as_view(),name='user_list'),
    path('users/<int:id>/',UserView.as_view(),name='user_process'),
    path('login',LoginView.login,name="login_view")
]

