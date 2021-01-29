from django.urls import path
from .views import ImageDetectionPOST, ListAllRecognitionImages

urlpatterns = [
    path('image/', ImageDetectionPOST.as_view(), name='image-detection-post'),
    path('results/', ListAllRecognitionImages.as_view(), name='image-ddetection-results')
]