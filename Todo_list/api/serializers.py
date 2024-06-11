from rest_framework import serializers
from tasks.models import TaskModel
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'  # or list the specific fields you want to include

class ResgisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("username is already taken")

        if data['email']:
            if User.objects.filter(username = data['email']).exists():
                raise serializers.ValidationError("email is already taken")
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
