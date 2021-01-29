from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DetectionImages


class ImagePOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetectionImages
        fields = ('input_image',)

    def create(self, validated_data):
        owner_id = self.context.get('owner')
        user = User.objects.get(id=owner_id)
        validated_data['owner'] = user
        return DetectionImages.objects.create(**validated_data)


class ImagePOSTResponseSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = DetectionImages
        fields = ('pk', 'owner', 'input_image', 'downloaded_at', 'status')

    def get_owner(self, obj):
        return obj.owner.username


class ProcessedImagesListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = DetectionImages
        fields = ('pk', 'owner', 'input_image', 'downloaded_at', 'status', 'output_image')

    def get_owner(self, obj):
        return obj.owner.username
