from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


User = settings.AUTH_USER_MODEL


class UrlObject(models.Model):
    """A single url"""

    user = models.ForeignKey(
        User,
        default=1,
        null=False,
        on_delete=models.CASCADE
    )
    long_url = models.URLField(
        null=False,
        blank=False
    )
    short_path = models.CharField(
        max_length=5,
        null=False,
        unique=True
    )
    added = models.DateTimeField(
        auto_now_add=True
    )
    public = models.BooleanField(
        default=True
    )
    clicks = models.PositiveIntegerField(
        default=0,
        null=False
    )
    tags = ArrayField(
        models.CharField(max_length=15),
        null=True,
        blank=True
    )

    class Meta:

        def __str__(self):
            return self.long_url
