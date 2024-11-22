from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('submit_contact_form/', views.submit_contact_form, name='submit_contact_form'),
    path('subscribe_newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
]
