from .models import Menu,Booking
from rest_framework import serializers
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'inventory'] 
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model
        fields = '__all__' 