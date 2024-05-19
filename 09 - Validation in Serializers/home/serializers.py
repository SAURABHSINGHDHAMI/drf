from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

    def validate(self, data):
        special_characters = "@#$%^&*()+=-[]{};:'\"\\|,<.>/?"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name cannot contain special chars')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        
        return data