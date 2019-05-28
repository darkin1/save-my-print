from rest_framework import serializers

class NewsletterSerializer(serializers.Serializer):
    email = serializers.EmailField()