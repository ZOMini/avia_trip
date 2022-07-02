from rest_framework.serializers import ModelSerializer

from trip.models import Airport, Company, Pass_in_trip, Plane, Trip


class TripSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Trip

class Pass_in_tripSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Pass_in_trip

class AirportSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Airport

class PlaneSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Plane

class CompanySerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Company
