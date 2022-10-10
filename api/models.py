from audioop import reverse
from django.db import models

# Create your models here.
class Person(models.Model):
    '''
    :Model: Model fields for Person
    '''
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


    def get_absolute_url(self):
        return reverse('person-details', args=[str(self.id)])
    

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
        
