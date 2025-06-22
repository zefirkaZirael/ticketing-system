from django.urls import path
from .views import RegisterView, TicketListCreateView, OrderListCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
