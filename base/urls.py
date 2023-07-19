from django.urls import path
from . import views

urlpatterns = [

path('',  views.home, name='home'),
path('suggestion/<str:pk>/', views.suggestion, name='suggestion'),

path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('about/', views.about, name='about'),

path('create-suggestion/', views.createSuggestion, name='create-suggestion'),
path('update-suggestion/<str:pk>/', views.updateSuggestion, name='update-suggestion'),
path('delete-suggestion/<str:pk>/', views.deleteSuggestion, name='delete-suggestion'),



]
