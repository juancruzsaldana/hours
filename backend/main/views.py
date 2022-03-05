
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from services.google import GoogleService
from services.toggl import TogglService
from main.serializers import TaskSerializer
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
class HomeView(TemplateView):
	template_name = "index.html"
	
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
	def index(request):
		cwd = GoogleService.connect_to_google_sheet('estimacion ver')
		print(cwd)
		# toggl = TogglService().get_time_entries()
		# print(toggl)
		context = {'cwd': 'datos'}
		return render(request, 'index.html', context)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getTasksView(request, format=None):
	if request.method == 'GET':
		start_date = request.query_params.get('start_date')
		end_date = request.query_params.get('end_date')
		
		queryset = TogglService().get_time_entries(start_date, end_date)
		serializer = TaskSerializer(queryset, many=True)
		tasklist = list(serializer.data)
		values = set(map(lambda x:x['pid'], tasklist))
		newlist = [[ y for y in tasklist if y['pid']==x] for x in values]
		groupedList = []

		for taskgroup in newlist:
			groupedList.append({'pid':taskgroup[0]['pid'], 'tasks':taskgroup})

		return Response(groupedList)
		