from rest_framework import serializers
from .models import User
from .models import Order, Ticket, CulturalObject
import random
import string

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
        read_only_fields = ['qr_code', 'user', 'order']


class OrderSerializer(serializers.ModelSerializer):  # "переводчик" модели Order в JSON и обратно.
    tickets = serializers.ListField(write_only=True)  # список объектов с данными билетов from user
    created_tickets = TicketSerializer(many=True, read_only=True, source='tickets')

    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        tickets_data = validated_data.pop('tickets') # вытаскиваешь список билетов из данных запроса.
        user = self.context['request'].user #  Берём текущего авторизованного пользователя, чтобы указать, кто оформил заказ и билеты
        order = Order.objects.create(user=user, **validated_data) # Создаём новый заказ в базе данных.

        for ticket_data in tickets_data: # Проходимся по каждому билету, который клиент отправил
            Ticket.objects.create( # Создаём один Ticket
                order=order,  # Привязываем его к только что созданному order
                user=user,  # Привязываем его к текущему user
                cultural_object_id=ticket_data['cultural_object'],
                visit_date=ticket_data['visit_date'],
                visit_time=ticket_data['visit_time'],
                qr_code=self._generate_qr_code()
            )
        return order # Возвращаем созданный зака, a DRF дальше сам сериализует этот order 
                        #  И автоматически покажет created_tickets (связанные билеты)


    def _generate_qr_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=12))