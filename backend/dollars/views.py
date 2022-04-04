from rest_framework.decorators import api_view
from rest_framework.response import Response
from dollars.serializers import MovementSerializer, SourcesSerializer, MovementDetailSerializer
from dollars.models import Movement, Sources, MovementDetail 
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
# Create your views here.

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
class Dollars (APIView):
    def get(self, request, format=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        # queryset = Expense.objects.filter(Q(end__gte=start_date) | Q(end__isnull=True) , Q(start__lte=end_date) | Q(start__isnull=True))
        # read_serializer = ExpenseSerializer(queryset, many=True)
        queryset = Movement.objects.all()
        read_serializer = MovementSerializer(queryset, many=True)
        return Response(read_serializer.data) 

    def post (self, request, format=None):
        create_serializer = MovementSerializer(data=request.data)
        if create_serializer.is_valid():
            created_movement = create_serializer.save()
            new_movement = MovementSerializer(created_movement).data
            return Response({"message": "Movement created successfully", "movement": new_movement})
        else:
            return Response({"message": "Movement not created", "errors": create_serializer.errors})

    def put (self, request, movement_id, format=None):
        movement = Movement.objects.get(id=movement_id)
        update_serializer = MovementSerializer(movement, data=request.data)
        if update_serializer.is_valid():
            updated_movement = update_serializer.save()
            updated_movement = MovementSerializer(updated_movement).data
            return Response({"message": "Movement updated successfully", "movement": updated_movement})
        else:
            return Response({"message": "Movement not updated", "errors": update_serializer.errors})
    
    def delete (self, request, movement_id, format=None):
        movement = Movement.objects.get(id=movement_id)
        movement.delete()
        return Response({"message": "Movement deleted successfully"})

class Source (APIView):
    def get(self, request, format=None):
        queryset = Sources.objects.all()
        read_serializer = SourcesSerializer(queryset, many=True)
        return Response(read_serializer.data) 

    def post (self, request, format=None):
        create_serializer = SourcesSerializer(data=request.data)
        if create_serializer.is_valid():
            created_source = create_serializer.save()
            new_source = SourcesSerializer(created_source).data
            return Response({"message": "Source created successfully", "source": new_source})
        else:
            return Response({"message": "Source not created", "errors": create_serializer.errors})

    def put (self, request, source_id, format=None):
        source = Sources.objects.get(id=source_id)
        update_serializer = SourcesSerializer(source, data=request.data)
        if update_serializer.is_valid():
            updated_source = update_serializer.save()
            updated_source = SourcesSerializer(updated_source).data
            return Response({"message": "Source updated successfully", "source": updated_source})
        else:
            return Response({"message": "Source not updated", "errors": update_serializer.errors})
    
    def delete (self, request, source_id, format=None):
        source = Sources.objects.get(id=source_id)
        source.delete()
        return Response({"message": "Source deleted successfully"})

class MovementDetails (APIView):
    def get(self, request, format=None):
        queryset = MovementDetail.objects.all()
        read_serializer = MovementDetailSerializer(queryset, many=True)
        return Response(read_serializer.data) 

    def post (self, request, format=None):
        create_serializer = MovementDetailSerializer(data=request.data)
        if create_serializer.is_valid():
            created_movement_detail = create_serializer.save()
            new_movement_detail = MovementDetailSerializer(created_movement_detail).data
            return Response({"message": "Movement detail created successfully", "movement_detail": new_movement_detail})
        else:
            return Response({"message": "Movement detail not created", "errors": create_serializer.errors})

    def put (self, request, movement_detail_id, format=None):
        movement_detail = MovementDetail.objects.get(id=movement_detail_id)
        update_serializer = MovementDetailSerializer(movement_detail, data=request.data)
        if update_serializer.is_valid():
            updated_movement_detail = update_serializer.save()
            updated_movement_detail = MovementDetailSerializer(updated_movement_detail).data
            return Response({"message": "Movement detail updated successfully", "movement_detail": updated_movement_detail})
        else:
            return Response({"message": "Movement detail not updated", "errors": update_serializer.errors})
    
    def delete (self, request, movement_detail_id, format=None):
        movement_detail = MovementDetail.objects.get(id=movement_detail_id)
        movement_detail.delete()
        return Response({"message": "Movement detail deleted successfully"})