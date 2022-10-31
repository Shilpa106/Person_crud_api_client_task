"""Person_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import *

from rest_framework import permissions
from drf_yasg import openapi
from rest_framework.schemas import get_schema_view
# from api.schema_d import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('persons', PersonApiView.as_view(),name='get-persons'),
    path('persons/<int:pk>/',PersonDetailView.as_view(),name='person-details'),
    

    path('schema',get_schema_view(
        title="Persons",
        version="1.0.0"
    ),  name='openapi-schema',),
    
    # path('v1/openapi', get_schema_view(generator_class=schema.SchemaGenerator, public=True),
    #      name='openapi-schema'),


    
]
