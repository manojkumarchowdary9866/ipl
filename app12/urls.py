from app12.views import iyer
from django.urls import path
app_name='app12'
urlpatterns=[
    path('iyer/',iyer,name='iyer'),
]