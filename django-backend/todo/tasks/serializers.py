from rest_framework import serializers
from .models import Task, Category
from categories.serializers import CategorySerializer


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, write_only=True)
    category_details = CategorySerializer(source='category', many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        categories = validated_data.pop('category')
        task = Task.objects.create(**validated_data)
        task.category.set(categories)
        return task
