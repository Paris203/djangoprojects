from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('display_date/', views.display_date),
    path('form_view/', views.form_view),
    path('about/', views.about),
    path('menu_card/', views.menu_by_id),
    path('menu/', views.menu),
]