from rest_framework import serializers, fields
from .models import Expense, Payment


class ChoicesSerializerField(serializers.SerializerMethodField):
    """
    A read-only field that return the representation of a model field with choices.
    """

    def to_representation(self, value):
        # sample: 'get_XXXX_display'
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        # retrieve instance method
        method = getattr(value, method_name)
        # finally use instance method to return result of get_XXXX_display()
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
