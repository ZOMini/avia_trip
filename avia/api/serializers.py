from rest_framework.serializers import (
    ListSerializer,
    ModelSerializer,
    PrimaryKeyRelatedField
)

from trip.models import Airport, Company, Pass_in_trip, Plane, Trip
from users.models import User


# for __Pass_in_tripSerializer__
class PassangerUserSerialiser(ModelSerializer):
    class Meta:
        fields = ['username', 'first_name','last_name']
        read_only_fields = ['__all__',]
        model = User

class TripSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        # read_only_fields = ['account_name']
        model = Trip
        depth = 1

class Pass_in_tripSerializer(ModelSerializer):
    passenger = PassangerUserSerialiser()
    
    class Meta:
        fields = '__all__'
        model = Pass_in_trip
        depth = 1

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
