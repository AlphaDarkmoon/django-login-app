from django.contrib import admin
from django.urls import path
from testmain_app import views

# Set the app name for namespacing the URLs
app_name = 'testmain_app'

# Define URL patterns for the 'testmain_app'
urlpatterns = [
    # URL pattern for the home view (accessible at '/')
    path('', views.home, name='home'),
    # URL pattern for the home view (accessible at '/home')
    path('home', views.home, name='home'),
]
