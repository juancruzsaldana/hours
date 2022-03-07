from email.policy import default
from enum import unique
from rest_framework import serializers

class TaskSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    guid = serializers.CharField()
    wid = serializers.IntegerField()
    billable = serializers.BooleanField()
    start = serializers.DateField()
    stop = serializers.DateField()
    duration = serializers.CharField()
    description = serializers.CharField()
    duronly = serializers.BooleanField()
    at = serializers.DateField()
    uid = serializers.IntegerField()
    pid = serializers.IntegerField(default = 0)
   