from pathlib import Path
import requests
from requests.auth import HTTPBasicAuth

from dotenv import load_dotenv, find_dotenv
import os

class TogglService:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.api_token =  os.getenv('TOGGL_API_TOKEN')
        self.base_url = 'https://api.track.toggl.com/api/v8/'
        self.headers = {
            'Authorization': 'Basic ' + self.api_token,
            'Content-Type': 'application/json'
        }

    def get_workspaces(self):
        url = self.base_url + '/workspaces'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_workspace_id(self, workspace_name):
        workspaces = self.get_workspaces()
        for workspace in workspaces:
            if workspace['name'] == workspace_name:
                return workspace['id']

    def get_projects(self, workspace_id):
        url = self.base_url + '/workspaces/{}/projects'.format(workspace_id)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_id(self, workspace_id, project_name):
        projects = self.get_projects(workspace_id)
        for project in projects:
            if project['name'] == project_name:
                return project['id']

    def get_project_tasks(self, workspace_id, project_id):
        url = self.base_url + '/workspaces/{}/projects/{}/tasks'.format(workspace_id, project_id)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_task_id(self, workspace_id, project_id, task_name):
        tasks = self.get_project_tasks(workspace_id, project_id)
        for task in tasks:
            if task['name'] == task_name:
                return task['id']

    def get_time_entries(self, start_date, end_date):
        url = self.base_url + '/time_entries?start_date='+start_date+'&end_date='+end_date
        response = requests.get(url, headers=self.headers, auth=HTTPBasicAuth(self.api_token, 'api_token'))
        return response.json()
    def get_project_by_id(self, project_id):
        url = self.base_url + '/projects/{}'.format(project_id)
        response = requests.get(url, headers=self.headers, auth=HTTPBasicAuth(self.api_token, 'api_token'))
        return response.json()
        