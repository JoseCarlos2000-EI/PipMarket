from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='principal'),
    path('login/',views.login,name='login'),
    path('products/',views.list_products,name='products'),
]