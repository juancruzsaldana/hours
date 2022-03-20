from rest_framework import serializers
from .models import Expense, Payment


class ChoicesSerializerField(serializers.SerializerMethodField):
    def to_representation(self, value):
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        method = getattr(value, method_name)
        return method()

class ExpenseSerializer(serializers.ModelSerializer):
    type_choices = serializers.SerializerMethodField()
    
    class Meta:
        model = Expense
        fields = ('id', 'name', 'start', 'end', 'type', 'type_choices', 'amount', 'description', 'get_type_display')
    

    def get_type_choices(self, obj):
        return [{'value': choice[0], 'name': choice[1]} for choice in Expense.EXPENSES_TYPES]



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
