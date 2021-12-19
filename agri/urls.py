from django.urls import path
from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    
    path("login",views.user_login,name='login'),
    path("maps",views.maps,name='maps'),
     path("scrape",views.scrape,name='srape'),
    path("weather",views.weatherFore,name = 'weather'),
    path("scrape_post",views.scrape_post,name="scrape_post"),
    path("log",views.logingout,name="logout"),
    path("dtail/<int:id>",views.dtail,name="dtail"),
    path("register",views.registration,name="uregister"),
    path("deregis",views.eregistration,name="eregister"),
    path("cropadd",views.addcrop,name="cropadd"),
    path("landing",views.landing,name="landing"),
    path('blogs/',views.postmaker,name='blogs'),
    path('newpost/',views.newposter,name='poster'),
    path('blogs/publish/<int:pk>/',views.publish,name='publish'),
    path('blogs/newpost/comment/<int:pk>/',views.comments,name='comments'),
    path("cropss",views.cropss,name="cropps")
]

