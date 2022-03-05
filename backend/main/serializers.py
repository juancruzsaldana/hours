from enum import unique
from rest_framework import serializers

class TaskItemSerializer(serializers.Serializer):
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
    pid = serializers.IntegerField()

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
    pid = serializers.IntegerField()
    # def group_by_pid(self, instance):
    #     filtered  = filter(lambda x: x['pid'] == instance['pid'], self.__dict__.get('_args')[0])
    #     project_tasks = list(filtered)
    #     # remaining = filter(lambda x: x['pid'] != instance['pid'], self.__dict__.get('_args')[0])
    #     # remaining_tasks = list(remaining)
    #     task_serializer = TaskItemSerializer(project_tasks, many=True)
    #     return task_serializer.data 
    # def to_representation(self, instance):
    #     output = {}
    #     filtered  = filter(lambda x: x['pid'] == instance['pid'], self.__dict__.get('_args')[0])
    #     project_tasks = list(filtered)

    #     for attribute in instance:
    #         if attribute == 'pid':
    #             pid = instance[attribute]
    #             if(pid in output):
    #                 output[pid].add(instance)
    #             else:
    #                 output[pid] = [instance]
    #     return output
    def to_internal_value(self, data):
        print('hola')
        print(self.get('pid'))
        return data