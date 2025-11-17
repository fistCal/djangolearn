from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_testapp, name ='all_testappp'),
    path('<int:seat_id>/', views.seat_detail, name ='seat_detail'),
    
]