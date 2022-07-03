from django import forms

from trip.models import Pass_in_trip


class Pass_in_tripForm(forms.ModelForm):
    class Meta:
        model = Pass_in_trip
        fields = ('place', 'trip')
