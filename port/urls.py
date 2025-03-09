from django.urls import path
from .import views
urlpatterns =[
   path('', views.name,name='home'),
   path('project/',views.project,name='project'),
   path('contact/',views.contact,name='contact'),
   path('about/',views.about,name='about'),

]