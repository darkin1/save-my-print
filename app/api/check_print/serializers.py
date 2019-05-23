from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(use_url=False)
    # aaa = serializers.FileField(use_url=False)