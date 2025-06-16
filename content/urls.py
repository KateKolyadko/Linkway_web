from django.urls import path
from . import views

app_name = 'content' 

urlpatterns = [
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/<slug:slug>/', views.vendor_detail, name='vendor_detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),

    path('news/<int:pk>/registrations/', 
         views.NewsRegistrationsView.as_view(), 
         name='news_registrations'),
]