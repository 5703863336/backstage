import re

from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','mobile','email','password')

        extra_kwargs = {

            'password':{
                'write_only':True,
                'max_length':20,
                'min_length': 8
            },
            'username':{
                'max_length': 20,
                'min_length': 4,
            }
        }

    def validate_mobile(self, attrs):

        if not re.match(r'1[3-9]\d{9}',attrs):
            raise serializers.ValidationError('手机格式不正确')

        return attrs
    def create(self, validated_data):

        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
