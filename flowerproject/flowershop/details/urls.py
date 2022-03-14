from . import views
from django.urls import path
app_name='details'


urlpatterns = [
    path('add', views.add,name='add'),
    path('login', views.login,name='login'),
    path('logout', views.logout, name='logout'),

]