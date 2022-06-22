from django.urls import path
from trip import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('airport/<int:airport_id>/', views.airport, name='airport'),
    path('in_airport/<int:airport_id>/', views.in_airport, name='in_airport'),
]
