
from django.urls import path
from website.views import *

urlpatterns = [
    path('', main, name="home"),  
    path('compiled', compile, name='compile'),
    path('download/<filename>', download_file)
]
