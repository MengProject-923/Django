from rest_framework import serializers
from .models import Users, Serverhosts, Fixedassets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ServerhostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serverhosts
        fields = '__all__'

class FixedassetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixedassets
        fields = '__all__'
