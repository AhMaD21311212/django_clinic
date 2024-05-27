from django.urls import path
from . import views

app_name = 'Doctor'
urlpatterns =[
    path('about', views.about.as_view(), name='about'),
    path('service', views.service.as_view(), name='service'),
    path('contact', views.ContactView, name='contact'),
]