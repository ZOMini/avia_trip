from rest_framework.serializers import ModelSerializer, StringRelatedField

from api.sub_serializers import PassangerUserSerialiser
from trip.models import Airport, Company, Pass_in_trip, Plane, Trip


class AirportSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Airport

class TripWriteSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        read_only = ['company','plane','airport_from','airport_to']
        model = Trip

class TripReadSerializer(ModelSerializer):
    company = StringRelatedField()
    plane = StringRelatedField()
    airport_from = StringRelatedField()
    airport_to = StringRelatedField()
    
    class Meta:
        fields = '__all__'
        read_only = ['company','plane','airport_from','airport_to']
        model = Trip

class Pass_in_tripSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Pass_in_trip
        read_only = ['passenger','trip']
        # depth = 2

class PlaneSerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Plane

class CompanySerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Company
