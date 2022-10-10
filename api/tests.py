# from django.test import TestCase, Client
# from django.urls import reverse
# from api.models import Person
# from api.serializers import *
# from rest_framework import status
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient, APITestCase
# import json
# import pdb
# import io


# # Test to GET data API

# class GetAllPersonTest(APITestCase):
#     ''' Test Module for GET all Person List '''

#     def setUp(self):
#         self.client = APIClient()
#         self.api_urls = reverse('person')

#         Person.objects.create(first_name='sakshi',last_name='chouhan', email="sakshi@gmail.com")

       
    
#     def test_get_all_person(self):
#         # get  API response
#         response = self.client.get(self.api_urls)

#         # get Data from Db
#         persons = Person.objects.all()
#         serializer = PersonSerializers(persons, many=True)

#         self.assertEquals(response.data, serializer.data)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)





# # modelssssssssssssssssss
# from django.test import TestCase
# from api.models import Person

# class TestPersonModels(TestCase):
#     '''Testing cases for Person models'''

#     def setUp(self):
#         self.person=Person.objects.create(first_name='sakshi',last_name='chouhan', email="sakshi@gmail.com")

#     def test_person_model_feilds(self):
#         self.assertEquals(str(self.person.first_name), 'sakshi')
#         self.assertEquals(str(self.person.last_name), 'chouhan')
#         self.assertEquals(str(self.person.email), 'sakshi@gmail.com')

# # urlsssssssssssssssssss

# from django.test import TestCase, SimpleTestCase
# from django.urls import reverse, resolve
# from api.views import *

# '''
#     Test Case for url testing.

#     If the views are class based  then after .func use .view_class

#     If url contains any slug or any id then inside the reverse function use args=[id or slug]

# '''

# class TestPersonUrls(SimpleTestCase):
#     '''
#     Test Cases for URL testing of GET, POST, PUT, DELETE for Category Urls
#     '''

#     def test_url_person_resolved(self):
#         url = reverse('person')

#         self.assertEquals(resolve(url).func.view_class, PersonApiView)

    
#     def test_url_categoty_details_resolved(self):
#         url = reverse('person-details', args=[20])

#         self.assertEquals(resolve(url).func.view_class, PersonDetailView)
