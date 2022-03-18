from app11.views import panth
from django.urls import path
app_name='app11'
urlpatterns=[
    path('panth/',panth,name='panth'),
]