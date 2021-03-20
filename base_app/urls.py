from django.urls import path
from  . import views
name = 'base_app'

urlpatterns =[
    path('', views.top, name='top'),
]
