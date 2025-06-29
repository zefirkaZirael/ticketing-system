from django.contrib.auth.models import AbstractUser
from django.db import models

# Пользователь
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Заказ (платёж)
class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.user.email}"


# Objects
class CulturalObject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    work_time = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Билет
class Ticket(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tickets')
    cultural_object = models.ForeignKey(CulturalObject, on_delete=models.CASCADE, related_name='tickets')
    visit_date = models.DateField()
    visit_time = models.TimeField()
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    is_used = models.BooleanField(default=False)
    cultural_object = models.ForeignKey(
    CulturalObject,
    on_delete=models.CASCADE,
    related_name='tickets'
    )
    def __str__(self):
        return f"Ticket #{self.id} for {self.cultural_object_name}"




