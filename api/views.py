
# Create your views here.
from . models import Person
from .serializers import PersonSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.schemas import ManualSchema


# from rest_framework 
from rest_framework.schemas import AutoSchema

import coreapi
import coreschema
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import renderers, response


from rest_framework.schemas import SchemaGenerator# field_to_schema
from rest_framework import serializers
import coreschema, coreapi

class ResponseMetaSchemaGenerator(SchemaGenerator):
    def get_operation_id(self, operation_keys):
      operation_id = 'shilpi'
      return operation_id


    # def get_response_fields(self, path, method, view):
    #     """
    #     return field descriptions for the response
    #     """
    #     if not hasattr(view, 'get_serializer'):
    #         return []

    #     serializer = view.get_serializer()

    #     if not isinstance(serializer, serializers.Serializer):
    #         return []

    #     fields = []
    #     for field in serializer.fields.values():
    #         if field.write_only:
    #             continue

    #         field = coreapi.Field(
    #             name=field.field_name,
    #             location='response',
    #             required=False,
    #             schema=field_to_schema(field)
    #         )
    #         fields.append(field)

    #     return fields

    def get_link(self, path, method, view):
        link = super(ResponseMetaSchemaGenerator, self).get_link(path, method, view)
        link._fields = link._fields + tuple(self.get_response_fields(path, method, view))
        return link

class PersonApiView(APIView):
    schema = ResponseMetaSchemaGenerator()
    # metadata_class = PersonApiViewMetadata
  


    def get(self, request, *args, **kwargs):

        '''
        Get list of persons
        
        '''

        userdetail = Person.objects.all()
        serializer = PersonSerializers(userdetail, many=True)

    
        data = {
                "description": "ok",
                "items": serializer.data
                }

            
        return Response(data,status=status.HTTP_200_OK)


    


    def post(self, request, *args, **kwargs):

        '''
        :Process: Post a Person 
        :summary: "Create New User"
        :method: `POST`
        :HTTPRequest:

        ** Context **
        
        :firstName:          `string`
        :lastName:           `string`
        :email:              `string`
        :Response: `Posted Data in Json`
        '''
        

        try:
            if Person.objects.filter(email=request.data.get("email")).exists():
                return Response({"description": "Email Already Taken"},status=status.HTTP_409_CONFLICT)

                     

        
            serializer_obj = PersonSerializers(data=request.data)
            if serializer_obj.is_valid():
                serializer_obj.save()

                data={

                    "description": "User Created",
                    "items": serializer_obj.data
                    }
                return Response(data, status=status.HTTP_200_OK)
            return Response({"errors":serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"description":"Missing Required Information"}, status=status.HTTP_400_BAD_REQUEST)
        



class PersonDetailView(APIView):
    # metadata_class = APIRootMetadata
    def get(self, request, *args, **kwargs):

        '''
        :Process: Person details
        :method: `GET`
        :HTTPRequest:
       

        ** Context **
        :param: `id`

        :Response: `Retrieve List of Json Array Data by ID, And Status Code According method`
        '''

       
        id = self.kwargs.get("pk")       
        
        if id is not None:           
            try:
                user_detail = Person.objects.get(id=id)
                serializer = PersonSerializers(user_detail)
                data = {
                    "description": "User Found",
                    "items": [serializer.data]
                }
                
                return Response(data,status=status.HTTP_200_OK)
            except Person.DoesNotExist:
                return Response({"description":"User not Found"},status=status.HTTP_404_NOT_FOUND)



    
    def put(self, request, *args, **kwargs):
        
        '''
        :Process: Person details
        :method: `PUT`
        :HTTPRequest:

        ** Context **
        :param: `id`

        :Response: `Retrieve List of Json Array Data by ID, And Status Code According method`
        '''

        id = self.kwargs.get("pk")
        try:
            user_det = Person.objects.get(id=id)
            userserializer = PersonSerializers(user_det, data=request.data)
            if userserializer.is_valid():
                userserializer.save()
                data = {
                    "description": "ok",
                    "items": [userserializer.data]
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response({"errors":userserializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response({"description": "User Not Found"},status=status.HTTP_404_NOT_FOUND)

    

    
    def delete(self, request, *args, **kwargs):


        '''
        :Process: Person details
        
        :method: `DELETE`
        :HTTPRequest:

        ** Context **
        :param: `id`
        :"description": "Remove person specified by id"

    
        '''

        id = self.kwargs.get("pk")
        try:
            userdetail = Person.objects.get(id=id)

            deleted_item={'userdetail':str(userdetail)}
            
            
            data = {
                "description": "ok",
                "items": [deleted_item]
            }

            userdetail.delete()
            return Response(data,status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response({"description": "Person does not exist with specified id"},status=status.HTTP_400_BAD_REQUEST)


