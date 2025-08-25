# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem, ShippingMethod

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = ['id', 'name', 'description', 'price', 'estimated_delivery']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'user', 'user_email', 'status', 'total_amount',
            'shipping_address', 'billing_address', 'created_at', 'updated_at', 'items'
        ]
        read_only_fields = ['order_number', 'user', 'total_amount', 'created_at', 'updated_at']