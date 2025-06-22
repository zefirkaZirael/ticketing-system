from rest_framework import serializers
from .models import User
from .models import Ticket, Order

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
