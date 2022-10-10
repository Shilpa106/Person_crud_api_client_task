
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from api.views import *

'''
    Test Case for url testing.

    If the views are class based  then after .func use .view_class

    If url contains any slug or any id then inside the reverse function use args=[id or slug]

'''

class TestPersonUrls(SimpleTestCase):
    '''
    Test Cases for URL testing of GET, POST, PUT, DELETE for Category Urls
    '''

    def test_url_person_resolved(self):
        url = reverse('person')

        self.assertEquals(resolve(url).func.view_class, PersonApiView)

    
    def test_url_categoty_details_resolved(self):
        url = reverse('person-details', args=[20])

        self.assertEquals(resolve(url).func.view_class, PersonDetailView)
