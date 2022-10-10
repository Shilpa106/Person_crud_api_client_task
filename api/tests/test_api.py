import re
from unicodedata import category
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from api.models import Person
from api.serializers import *
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
import json



# Test to GET data API

class GetAllPersonTest(APITestCase):
    ''' Test Module for GET all Person List '''

    def setUp(self):
        self.client = APIClient()
        self.api_urls = reverse('person')

        Person.objects.create(first_name='sakshi',last_name='chouhan', email="sakshi@gmail.com")

       
    
    def test_get_all_person(self):
        # get  API response
        response = self.client.get(self.api_urls)

        # get Data from Db
        persons = Person.objects.all()
        serializer = PersonSerializers(persons, many=True)

        self.assertEquals(serializer.data, serializer.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class GetSinglePersonTest(APITestCase):
    '''Test Module for GET single Person API'''

    @classmethod

    def setUp(self):
        self.client=APIClient()

        self.person=Person.objects.create(first_name='saakshi',last_name='cahouhan', email="sakshi@gmail.com")

    def test_get_valid_single_person(self):
        # response = self.client.get(reverse('user-detail', args=[self.user.id]))
        response = self.client.get(reverse('person-details', args=[self.person.id]))
        
        person=Person.objects.get(id=self.person.id)
        serializer = PersonSerializers(person)

        self.assertEqual(serializer.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# check invalid condition
    def test_get_invalid_single_person(self):
        response = self.client.get(reverse('person-details', args=[29]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Test of POST data API

class CreateNewPersonTest(APITestCase):
    '''Test Module for inserting a new person'''

    def setUp(self):
        self.client=APIClient()
        self.person=Person.objects.create(first_name='sonkshi',last_name='cahoouhan', email="sonakshi@gmail.com")

        self.valid_payload={
            'person_id':self.person.id,
            'first_name':'shyam',
            'last_name':'yadav'
        }

        self.invalid_payload={
            'person_id':'',
            'first_name':'',
            'last_name':''
        }

    # def test_create_valid_person(self):
    #     response=self.client.post(reverse('person'),data=self.valid_payload,format='multipart')
    #     self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        response=self.client.post(reverse('person'),data=self.invalid_payload,format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Test of PUT or UPDATE API

class UpdateSinglePersonTest(APITestCase):
    '''Test module for updating an existing Person'''
    def setUp(self):
        self.client=APIClient()
        self.person=Person.objects.create(first_name='sonkshi',last_name='cahoouhan', email="sonakshi@gmail.com")
        
        self.valid_payload={
            'person_id':self.person.id,
            'first_name':'shyam',
            'last_name':'sssss'
        }

        self.invalid_payload={
            'person_id':'',
            'first_name':'',
            'last_name':''
        }

    def test_update_valid_person(self):
        response=self.client.put(reverse('person-details',args=[self.person.id]),data=self.valid_payload,format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_person(self):
        response=self.client.put(reverse('person-details',args=[self.person.id]),data=json.dumps(self.invalid_payload),content_type='Application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class DeleteSinglePersonTest(APITestCase):
    '''Test module for deleting an existing Person'''
    def setUp(self):
        self.client=APIClient()
        self.person=Person.objects.create(first_name='sonkshi',last_name='cahoouhan', email="sonakshi@gmail.com")
        
        
    def test_valid_delete_person(self):
        response=self.client.delete(reverse('person-details',args=[self.person.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_person(self):
        response=self.client.delete(reverse('person-details',args=[35]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        




