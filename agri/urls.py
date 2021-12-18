from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path("login",views.login,name='login'),
<<<<<<< HEAD
    path("maps",views.maps)
=======
    path("maps",views.maps,name='maps')
>>>>>>> 0a59a3de3b51343abb35eab5e593c8f83cbaedd7
]