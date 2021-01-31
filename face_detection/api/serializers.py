from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DetectionImages, DetectedFaces


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


class DetectedFacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetectedFaces
        fields = ('x1', 'y1', 'x2', 'y2')


class ProcessedImagesListSerializer(serializers.ModelSerializer):
    faces = serializers.SerializerMethodField()

    class Meta:
        model = DetectionImages
        fields = ('downloaded_at', 'output_image', 'faces')

    def get_faces(self, obj):
        faces = obj.detectedfaces_set.all()
        return DetectedFacesSerializer(
            faces, many=True,
            context={'request': self.context.get('request')}).data