from django.urls import path
from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path("login",views.user_login,name='login'),
    path("maps",views.maps,name='maps'),
    path("scrape",views.scrape,name="scrape"),
    path("weather",views.weatherFore,name = 'weather'),
    path("scrape_post",views.scrape_post,name="scrape_post"),
    path("log",views.logingout,name="logout"),
    path("dtail/<int:id>",views.dtail,name="dtail"),
    path("register",views.regist,name="eregister"),
    path("deregis",views.degrig,name="uregister")
]