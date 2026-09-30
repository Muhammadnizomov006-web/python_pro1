from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='index' ),
    path('checkout/', checkout, name='checkout'),
    path('blank/', blank, name='blank'),
    path('product/', product, name='product'),
    path('store/', store, name='store'),
    path('detalls/<int:pk>/',Detalles.as_view()),
    path('cheked/',Biling),
    path('tek/',Taj),
    path('search/',Search, name='Search'),
    path('sorov/',Qidiruv),
    path('login/',Login.as_view() , name='login'),
    path('register/',Register.as_view()),
]










