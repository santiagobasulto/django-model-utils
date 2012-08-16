import datetime
from django.db import models
from model_utils.models import SlugModel


class DummyModel(SlugModel, models.Model):
    name = models.CharField(max_length=60)


class DummyModelCustomName(SlugModel, models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        sluggify_for_me = "nombre"


class DummyModelCustomSave(SlugModel, models.Model):
    name = models.CharField(max_length=60)
    date_saved = models.DateTimeField()

    def get_date_to_save(self):
        return datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.date_saved = self.get_date_to_save()
        super(DummyModelCustomSave, self).save(*args, **kwargs)
