from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('organization/', views.organization, name='organization'),
    path('contact/', views.contact, name='contact'),

]