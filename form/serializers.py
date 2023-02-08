from rest_framework import serializers
from .models import CNABData, CNAB

class CNABSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNAB
        fields = ('id', 'file', 'processed')

class CNABDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNABData
        fields = ('id', 'type', 'data', 'value', 'cpf', 'card', 'hour', 'store_owner', 'store_name')

class Store(serializers.Serializer):
    store_name = serializers.CharField()