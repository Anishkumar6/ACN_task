from django.urls import path
from registration import views
urlpatterns = [path('', views.index, name='home')]