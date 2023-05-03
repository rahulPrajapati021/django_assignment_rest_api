from rest_framework import serializers
from .models import Work, Client

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields=('artist_name', 'link', 'work_type')
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('username', 'password')