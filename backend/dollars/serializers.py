from rest_framework import serializers
from .models import Movement, Sources, MovementDetail


class ChoicesSerializerField(serializers.SerializerMethodField):
     def to_representation(self, value):
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        method = getattr(value, method_name)
        return method()

class MovementSerializer(serializers.ModelSerializer):
    type_choices = serializers.SerializerMethodField()
    sellValue_choices = serializers.SerializerMethodField()
    class Meta:
        model = Movement
        fields = ('id', 'name', 'amountInDollars', 'amountInPesos', 'date', 'type', 'type_choices', 'get_type_display', 'sellValue', 'sellValue_choices', 'get_sellValue_display')

    def get_type_choices(self, obj):
        return [{'value': choice[0], 'name': choice[1]} for choice in Movement.MOVEMENT_TYPES]
    def get_sellValue_choices(self, obj):
        return [{'value': choice[0], 'name': choice[1]} for choice in Movement.MOVEMENT_SOURCES]

class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = '__all__'

class MovementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementDetail
        fields = '__all__'