from rest_framework import serializers
from ninorooms.models import NinoRooms



class NinoRoomsSerializer(serializers.ModelSerializer):
     class Meta:
        model = NinoRooms
        fields = ('id','pg_name', 'phone_number', 'owner_name', 
        'location','address','details','ac_prices','non_ac_prices','pg_image','pg_image_two','pg_image_three')