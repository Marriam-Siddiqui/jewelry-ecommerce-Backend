# payments/serializers.py
from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(source='order.order_number', read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 'order', 'order_number', 'payment_method', 'amount', 
            'status', 'transaction_id', 'created_at', 'updated_at'
        ]
        read_only_fields = ['amount', 'created_at', 'updated_at']