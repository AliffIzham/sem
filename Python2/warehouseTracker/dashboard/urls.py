from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('track/', views.track, name='track')
]

