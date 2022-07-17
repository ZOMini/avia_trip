from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

# for __Pass_in_tripSerializer__
class PassangerUserSerialiser(ModelSerializer):
    class Meta:
        fields = ['username', 'first_name','last_name']
        read_only_fields = ['__all__',]
        model = User


