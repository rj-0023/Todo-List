from rest_framework import serializers
from .models import TaskModel

class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'  # or list the specific fields you want to include
