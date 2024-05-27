from django.urls import path

from . import views

urlpatterns = [
    path('heure', views.current_datetime , name='home'),
    path('signup', views.sign_up , name='inscription'),
    path('login', views.log_in , name='Connexion'),
    path('logout', views.log_out , name='Déconnexion'),
]