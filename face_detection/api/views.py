from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ImagePOSTSerializer, ImagePOSTResponseSerializer, ProcessedImagesListSerializer
from .models import DetectionImages


@permission_classes([IsAuthenticated])
class ImageDetectionPOST(CreateAPIView):
    """
        View for image uploading
    """
    serializer_class = ImagePOSTSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'owner': request.user.id})
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(data=ImagePOSTResponseSerializer(obj).data,
                        status=status.HTTP_200_OK)


class ListAllRecognitionImages(ListAPIView):
    """
        List view for recognition results
    """

    serializer_class = ProcessedImagesListSerializer

    def get_queryset(self):
        return DetectionImages.objects.all().order_by('downloaded_at')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)