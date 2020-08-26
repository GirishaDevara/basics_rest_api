from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def create(self, validated_data):
        # Create and return a new `Article` instance, given the validated data.
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing `Article` instance, given the validated data.

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
