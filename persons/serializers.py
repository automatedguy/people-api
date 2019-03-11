from rest_framework import serializers
from persons import models


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'nickname',
            'first_name',
            'last_name',
            'birth_date',
            'creation_date',
            'active'
        )

        model = models.Person
