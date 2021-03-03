from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('/', product_list, name='product_list'),
    path('/<slug:product_slug>', product_detail, name='product_detail')

]