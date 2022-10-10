from rest_framework import serializers
from . models import Person



class PersonSerializers(serializers.ModelSerializer):

    '''
    :Serializer: Serializer fields for Person to serialize and deserialize json data
    '''
    # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     if not data['first_name']:
    #         raise serializers.ValidationError("first name is required")
    #     return data

    class Meta:
        
        model = Person
        fields = ("id","first_name", "last_name", "email")

    def validate(self, data):
        if not data['first_name']:
            raise serializers.ValidationError('firstname should be a string')
        return data
        
        

        