from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.departments,name='department'),
    path('doctors/',views.doctors,name='doctor'),
    path('about/',views.about,name='about'),
]
