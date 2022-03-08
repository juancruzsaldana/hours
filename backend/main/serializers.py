from email.policy import default
from enum import unique
from xml.dom.minidom import Document
from rest_framework import serializers

class TaskSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    guid = serializers.CharField()
    wid = serializers.IntegerField()
    billable = serializers.BooleanField()
    start = serializers.DateField()
    stop = serializers.DateField()
    duration = serializers.CharField()
    description = serializers.CharField(default = "No Description")
    duronly = serializers.BooleanField()
    at = serializers.DateField()
    uid = serializers.IntegerField()
    pid = serializers.IntegerField(default = 0)
   
class GDocsRequestSerializer (serializers.Serializer):
    document = serializers.CharField(default = "No Document")
    rate = serializers.FloatField(default = 0)
    structure = serializers.JSONField(default = {})