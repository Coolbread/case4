from django.conf import settings
from django.urls import path
from . import views

app_name = 'track_followers'

urlpatterns = [
	path('api/', views.api),
	path('test/', views.test)
]