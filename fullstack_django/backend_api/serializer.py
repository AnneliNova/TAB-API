from rest_framework import serializers
from .models import Chair, Table

class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = ['id', 'name', 'price', 'quantity']
