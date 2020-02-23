import uuid
from io import BytesIO
from PIL import Image
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from dual_rocks.authentication.models import User
from dual_rocks.utils import (
    apply_watermark,
    apply_blur
)


class ImageWithPrivacy(models.Model):
    class Meta:
        unique_together = ['user', 'content_type', 'instance_id', 'field']

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='images_with_privacy',
        null=True,
        blank=True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    instance_id = models.PositiveIntegerField()
    instance = GenericForeignKey('content_type', 'instance_id')
    field = models.CharField(
        _('campo'),
        max_length=255
    )
    processed_image = models.ImageField(_('imagem processada'))
    created_at = models.DateTimeField(
        _('criado em'),
        auto_now=True,
        editable=False
    )

    @classmethod
    def get_or_create(cls, user, instance, field):
        if user and user.is_anonymous:
            user = None
        content_type = ContentType.objects.get_for_model(instance.__class__)
        try:
            return cls.objects.get(
                user=user,
                content_type=content_type,
                instance_id=instance.id,
                field=field
            )
        except cls.DoesNotExist:
            image_field_file = getattr(instance, field)
            image = Image.open(image_field_file.file)

            if user:
                out_image = apply_watermark(image, user.email)
            else:
                out_image = apply_blur(image)

            out_image_io = BytesIO()
            out_image.save(out_image_io, format='JPEG')
            cls_instance = cls(
                user=user,
                content_type=content_type,
                instance_id=instance.id,
                field=field
            )
            cls_instance.processed_image.save(
                f'{user and user.id or "anonymous"}.{content_type}.'
                f'{instance.id}.{field}.{uuid.uuid4()}.jpg',
                File(out_image_io),
                save=False
            )
            cls_instance.save()
            return cls_instance
