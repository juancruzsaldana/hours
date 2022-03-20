from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from expenses.serializers import ExpenseSerializer, PaymentSerializer
from expenses.models import Expense, Payment
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getExpenses(request, format=None):
    if request.method == 'GET':
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        queryset = Expense.objects.filter(Q(end__gte=start_date) | Q(end__isnull=True) , Q(start__lte=end_date) | Q(start__isnull=True))
        
        read_serializer = ExpenseSerializer(queryset, many=True)
        return Response(read_serializer.data)
    elif request.method == 'POST':
        create_serializer = ExpenseSerializer(data=request.data)
        if create_serializer.is_valid():
            created_expense = create_serializer.save()
            new_expense = ExpenseSerializer(created_expense).data
            return Response({"message": "Expense created successfully", "expense": new_expense})
        else:
            return Response({"message": "Expense not created", "errors": create_serializer.errors})

@api_view(['PUT', 'DELETE'])
def operateExpense (request, expense_id, format=None):
    if request.method == 'PUT':
        expense = Expense.objects.get(id=expense_id)
        update_serializer = ExpenseSerializer(expense, data=request.data)
        if update_serializer.is_valid():
            updated_expense = update_serializer.save()
            updated_expense = ExpenseSerializer(updated_expense).data
            return Response({"message": "Expense updated successfully", "expense": updated_expense})
        else:
            return Response({"message": "Expense not updated", "errors": update_serializer.errors})
    elif request.method == 'DELETE':
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
        return Response({"message": "Expense deleted successfully"})

class Expensesoptions (APIView):
    def get(self, request, format=None):
        options = Expense.EXPENSES_TYPES
        return Response(options)
class Payments (APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    def get (self, request, format=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        queryset = Payment.objects.filter(Q(date__gte=start_date) | Q(date__isnull=True) , Q(date__lte=end_date) | Q(date__isnull=True))
        read_serializer = PaymentSerializer(queryset, many=True)
        return Response(read_serializer.data)

    def post (self, request, format=None):
        create_serializer = PaymentSerializer(data=request.data)
        if create_serializer.is_valid():
            created_payment = create_serializer.save()
            new_payment = PaymentSerializer(created_payment).data
            return Response({"message": "Payment created successfully", "payment": new_payment})
        else:
            return Response({"message": "Payment not created", "errors": create_serializer.errors})

    def put (self, request, payment_id, format=None):
        payment = Payment.objects.get(id=payment_id)
        update_serializer = PaymentSerializer(data=request.data, instance=payment)
        if update_serializer.is_valid():
            updated_expense = update_serializer.save()
            updated_expense = PaymentSerializer(updated_expense).data
            return Response({"message": "Payment updated successfully", "payment": updated_expense})
        else:
            return Response({"message": "Payment not updated", "errors": update_serializer.errors})

    def delete (self, request, payment_id, format=None):
        payment = Payment.objects.get(id=payment_id)
        payment.delete()
        return Response({"message": "Payment deleted successfully"})