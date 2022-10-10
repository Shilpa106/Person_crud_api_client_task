from dataclasses import field
from unittest.util import _MAX_LENGTH
from django.test import TestCase
from api.models import Person

class TestPersonModels(TestCase):
    '''Testing cases for Person models'''

    def setUp(self):
        self.person=Person.objects.create(first_name='sakshi',last_name='chouhan', email="sakshi@gmail.com")

    def test_person_model_fields(self):
        self.assertEquals(str(self.person.first_name), 'sakshi')
        self.assertEquals(str(self.person.last_name), 'chouhan')
        self.assertEquals(str(self.person.email), 'sakshi@gmail.com')



# test2***********************
class PersonModelTest(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        

        Person.objects.create(first_name='sakshi1',last_name='chouhan1', email="sakshi@gmail.com")

    def test_first_name_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        person=Person.objects.get(id=1)
        field_label=person._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label,'last name')

    def test_email_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_first_name_max_length(self):
        person=Person.objects.get(id=1)
        max_length=person._meta.get_field('first_name').max_length
        self.assertEqual(max_length,30)

    def test_last_name_max_length(self):
        person=Person.objects.get(id=1)
        max_length=person._meta.get_field('last_name').max_length
        self.assertEqual(max_length,30)

    def test_object_name_is_first_name_comma_last_name(self):
        person=Person.objects.get(id=1)
        expected_object_name=f'{person.first_name}, {person.last_name}'
        self.assertEqual(str(person), expected_object_name)

    def test_get_absolute_url(self):
        person=Person.objects.get(id=1)
        # this will also fail if the urlconf is not defined
        self.assertEqual(person.get_absolute_url(), '/persons/1/')





