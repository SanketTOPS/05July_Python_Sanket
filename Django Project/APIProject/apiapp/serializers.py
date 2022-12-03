from rest_framework import serializers
from .models import userinfo


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=userinfo
        fields='__all__'