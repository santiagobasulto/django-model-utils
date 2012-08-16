import datetime
from mock import patch
from django.test import TestCase
from model_utils.tests.models import (
    DummyModel, DummyModelCustomSave, DummyModelCustomName
)

MOCKED_DATETIME = datetime.datetime(year=1948, month=5, day=31)


class TestSluggifyModel(TestCase):

    def test_model_gets_sluggified_on_save(self):
        dummy = DummyModel(name="A weird name with spaces and a weird $ign")
        dummy.save()

        self.assertEqual(
            dummy.slug,
            "a-weird-name-with-spaces-and-a-weird-ign"
        )
        clazz = DummyModel
        self.assertEqual(clazz.objects.count(), 1)
        model = clazz.objects.all()[0]
        self.assertEqual(model.slug, "a-weird-name-with-spaces-and-a-weird-ign")
        self.assertEqual(model.name, "A weird name with spaces and a weird $ign")


    @patch.object(
        DummyModelCustomSave,
        'get_date_to_save',
        return_value=MOCKED_DATETIME
    )
    def test_model_with_custom_save_gets_sluggified_on_save(self, MockClass):
        dummy = DummyModelCustomSave(
            name="A weird name with spaces and a weird $ign"
        )
        dummy.save()

        self.assertEqual(
            dummy.slug,
            "a-weird-name-with-spaces-and-a-weird-ign"
        )
        self.assertEqual(dummy.date_saved, MOCKED_DATETIME)
        clazz = DummyModelCustomSave
        self.assertEqual(clazz.objects.count(), 1)
        model = clazz.objects.all()[0]
        self.assertEqual(model.slug, "a-weird-name-with-spaces-and-a-weird-ign")
        self.assertEqual(model.name, "A weird name with spaces and a weird $ign")

    def test_model_with_custom_name_gets_sluggified_on_save(self):
        dummy = DummyModelCustomName(
            nombre="A weird name with spaces and a weird $ign"
        )

        dummy.save()

        self.assertEqual(
            dummy.slug,
            "a-weird-name-with-spaces-and-a-weird-ign"
        )

        clazz = DummyModelCustomName
        self.assertEqual(clazz.objects.count(), 1)
        model = clazz.objects.all()[0]
        self.assertEqual(model.slug, "a-weird-name-with-spaces-and-a-weird-ign")
        self.assertEqual(model.nombre, "A weird name with spaces and a weird $ign")
