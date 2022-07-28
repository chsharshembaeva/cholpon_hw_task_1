from django.urls import path, include
from . import views

urlpatterns = [
    path('greetings/', views.greetings, name='greetings'),
    path('', views.list_item, name='index'),
    path('<id>/', views.detail_item, name='detail_item'),
]