from rest_framework import serializers
from .models import *


class CardsSerializer(serializers.HyperlinkedModelSerializer):
    usage_date = serializers.DateField(write_only=True)

    class Meta:
        model = Cards
        fields = (
            'id',
            'series',
            'number',
            'release_date',
            'activity_end_date',
            'status',
            'usage_date'
        )

    def create(self, validated_attrs):
        instance = Cards.objects.create(**validated_attrs)
        return instance
