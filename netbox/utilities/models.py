from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class CreatedUpdatedModel(models.Model):
    created = models.DateField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class TaggedModel(models.Model):
    tags = GenericRelation(
        to='extras.Tag',
        related_query_name='tags'
    )

    class Meta:
        abstract = True
