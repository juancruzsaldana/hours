
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