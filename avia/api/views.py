from rest_framework import viewsets

from api.permissions import AdminOrReadOnly
from api.serializers import (
    AirportSerializer,
    CompanySerializer,
    Pass_in_tripSerializer,
    PlaneSerializer,
    TripSerializer
)
from trip.models import Airport, Company, Pass_in_trip, Plane, Trip


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = (AdminOrReadOnly, )

class Pass_in_tripViewSet(viewsets.ModelViewSet):
    queryset = Pass_in_trip.objects.all()
    serializer_class = Pass_in_tripSerializer
    permission_classes = (AdminOrReadOnly, )

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = (AdminOrReadOnly, )

class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = (AdminOrReadOnly, )
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AdminOrReadOnly, )
