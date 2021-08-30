from django.db import models
from django.db.models import fields
from rest.models import Info
from rest_framework import serializers

class AddTwoNumberSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        print("Context on serializer",self.context)
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance

        # return super().update(instance, validated_data)

class InfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Info
        fields = ['name', 'address']