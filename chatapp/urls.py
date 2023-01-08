from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('clear_chat/', views.clear_chat, name='clear'),
]