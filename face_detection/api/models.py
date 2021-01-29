from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

IMAGE_STATUSES = (
    ('new', _('New')),
    ('processing', _('Processing')),
    ('finished', _('Finished'))
)


class DetectionImages(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    input_image = models.ImageField(upload_to=f'input_images/{owner}')
    downloaded_at = models.DateTimeField(auto_now_add=True)
    output_image = models.ImageField()
    status = models.CharField(choices=IMAGE_STATUSES, default='new', max_length=10)


class DetectedFaces(models.Model):
    x1 = models.IntegerField()
    x2 = models.IntegerField()
    y1 = models.IntegerField()
    y2 = models.IntegerField()
    detection_image = models.ForeignKey(DetectionImages, on_delete=models.CASCADE)