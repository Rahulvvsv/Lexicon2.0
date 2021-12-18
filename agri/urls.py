from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path("login",views.login,name='login'),
    path("maps",views.maps,name='maps'),
    path("scrape",views.scrape,name="scrape"),
    path("weather",views.weatherFore,name = 'weather'),
    path("scrape_post",views.scrape_post,name="scrape_post")
]