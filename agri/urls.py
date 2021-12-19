from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path("login",views.loggin,name='login'),
    path("maps",views.maps,name='maps'),
    path("scrape",views.scrape,name='srape'),
    path("weather",views.weatherFore,name = 'weather'),
    path("scrape_post",views.scrape_post,name='srape_post'),
    path("log",views.logingout,name="logout"),
    path("dtail/<int:id>",views.dtail,name="dtail")
]