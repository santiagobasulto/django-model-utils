from django.db import models
import django.db.models.options as options
from django.template.defaultfilters import slugify

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('sluggify_for_me',)


class SlugModel(models.Model):
    slug = models.CharField(max_length=255)

    def __get_attr_name(self):
        return (
            (
                hasattr(self._meta, 'sluggify_for_me') and
                self._meta.sluggify_for_me
            )
            or "name"
        )

    def save(self, *args, **kwargs):
        attr_name = self.__get_attr_name()
        value = getattr(self, attr_name)
        self.slug = slugify(value)
        for clazz in self.__class__.__bases__:
            if clazz != SlugModel:
                clazz.save(self, *args, **kwargs)

    class Meta:
        abstract = True
