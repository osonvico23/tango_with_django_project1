from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('', views.show_page, name = 'show_page'),
    path('add_category/', views.add_category, name='add_category'),
    ]
