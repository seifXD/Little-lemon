from .models import Menu,Booking
from rest_framework import serializers
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['url', 'username', 'email', 'groups'] 
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model
        fields = '__all__' 