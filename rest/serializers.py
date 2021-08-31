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
    message = serializers.SerializerMethodField()
    class Meta:
        model= Info
        fields = ['name', 'address','message']
    @staticmethod
    def get_message(obj):
        name = obj.name
        address = obj.address
        return f'Hi! My name is {name} and I live in {address}'
    @staticmethod
    # to validate only a single field
    def validate_name(name):
        if len(name) <= 1:
            raise serializers.ValidationError("Length of name shouldn't be greater that 1")
        return name

# to validate as a whole
    def validate(self, data):
        name = data['name']
        address = data['address']
        if name == address:
            raise serializers.ValidationError("Name and address should not be same")
        print(data)
        return(data)