from rest_framework import serializers
from .models import *


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ['file']


class DealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deals
        fields = ['customer', 'item', 'total', 'quantity', 'date']

