from rest_framework import serializers
from .models import MyModel
import random

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

    def create(self, validated_data):
        random_number = random.randint(0, 1)
        if random_number == 0:
            raise serializers.ValidationError("Creation not allowed. Random number generated is 0.")
        return super().create(validated_data)
