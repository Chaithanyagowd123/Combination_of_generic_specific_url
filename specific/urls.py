from django.urls import path
from specific.views import *
app_name='something'
urlpatterns=[
    path('jan/',jan,name='jan'),
    path('janu2/',janu2,name='janu2'),
]