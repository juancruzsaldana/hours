
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
from main.serializers import TaskSerializer, GDocsRequestSerializer
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.
class HomeView(TemplateView):
	template_name = "index.html"
	
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
		
	def index(request):
		try:
			cwd = GoogleService.connect_to_google_sheet('estimacion ver')
			# toggl = TogglService().get_time_entries()
			context = {'cwd': 'datos'}
			return render(request, 'index.html', context)
		except Exception as e:
			context = {'cwd': e}
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
			pid = taskgroup[0]['pid']
			if pid != 0:
				project = TogglService().get_project_by_id(pid)
			else:
				project = {'data':{'name': 'Agencia', 'id': 10, 'hex_color': "#dddddd"}}
				pid = 10
			groupedList.append({'pid':pid, 'tasks':taskgroup, 'project':project})

		return Response(groupedList)

@api_view(['GET'])
def getGdocsStructure (request, format=None):
	if request.method == 'GET':
		cwd = GoogleService().connect_to_google_sheet('estimacion ver','Sheet1')
		return Response(cwd)

@api_view(['POST', 'PUT', 'GET'])	
def writeGdocs (request, format=None):
	if request.method == 'POST':
		serializer = GDocsRequestSerializer(request.data)
		items = serializer.data
		filename = items['document']
		del items['document']
		gresponse = GoogleService().update_google_sheet(filename ,items)
		return Response(gresponse)
	if request.method == 'GET':
		cwd = GoogleService().connect_to_google_sheet('estimacion ver','Sheet1')
		return Response(cwd)
