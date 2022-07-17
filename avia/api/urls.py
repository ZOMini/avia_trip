from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    AirportViewSet,
    CompanyViewSet,
    Pass_in_tripViewSet,
    PlaneViewSet,
    TripViewSet
)

app_name = 'api'
router_v1 = DefaultRouter()
router_v1.register('trip', TripViewSet, 'trip')
router_v1.register('pass_in_trip', Pass_in_tripViewSet, 'pass_in_trip')
router_v1.register('airport', AirportViewSet, 'airport')
router_v1.register('plane', PlaneViewSet, 'plane')
router_v1.register('company', CompanyViewSet, 'company')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
