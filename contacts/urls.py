from django.urls import path
from .views import partnership_request, contacts_view

app_name = 'contacts' 

urlpatterns = [
    path('partnership_form/', partnership_request, name='partnership_form'),
    path('contacts/', contacts_view, name='contacts'),
]