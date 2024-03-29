from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('create/<int:id>/<int:success>', views.create, name='create'),
    path('create/<int:id>', views.create, name='create'),
]
