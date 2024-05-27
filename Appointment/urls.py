from django.urls import path
from . import views

app_name = 'appointment'
urlpatterns =[
    path('',views.AppointmentView.as_view(), name='appointment'),
    path('resid/<int:pk>',views.resid, name='resid'),
]