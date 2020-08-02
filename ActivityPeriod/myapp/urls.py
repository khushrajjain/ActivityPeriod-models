from django.urls import path

from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('generateuser/',views.generateuser,name='generateuser'),
    path('generateactivity/',views.generateactivity,name='generateactivity')
    
    
]