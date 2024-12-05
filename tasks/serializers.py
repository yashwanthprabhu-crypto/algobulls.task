from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'created', 'title', 'description', 'due_date', 'tags', 'status']

    def create(self, validated_data):
        # Handle nested tag creation
        tags_data = validated_data.pop('tags', [])
        task = Task.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            task.tags.add(tag)
        return task

    def update(self, instance, validated_data):
        # Handle tag updates
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        # Update tags
        if tags_data:
            instance.tags.clear()  # Remove old tags
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)
        return instance
