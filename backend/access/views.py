from django.shortcuts import render
from rest_framework.response import Response
from access.serializers import AccessSerializer
from access.models import Access as AccessModel
from rest_framework.views import APIView

class Access (APIView):
    def get (self, request, format=None):
        queryset = AccessModel.objects.all()
        read_serializer = AccessSerializer(queryset, many=True)
        return Response(read_serializer.data)

    def post (self, request, format=None):
        create_serializer = AccessSerializer(data=request.data)
        if create_serializer.is_valid():
            created_access = create_serializer.save()
            new_access = AccessSerializer(created_access).data
            return Response({"message": "Access created successfully", "access": new_access})
        else:
            return Response({"message": "Access not created", "errors": create_serializer.errors})

    def put (self, request, access_id, format=None):
        access = AccessModel.objects.get(id=access_id)
        update_serializer = AccessSerializer(data=request.data, instance=access)
        if update_serializer.is_valid():
            updated_access = update_serializer.save()
            updated_access = AccessSerializer(updated_access).data
            return Response({"message": "Access updated successfully", "access": updated_access})
        else:
            return Response({"message": "Access not updated", "errors": update_serializer.errors})

    def delete (self, request, access_id, format=None):
        access = AccessModel.objects.get(id=access_id)
        access.delete()
        return Response({"message": "Access deleted successfully"})
