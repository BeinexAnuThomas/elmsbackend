from rest_framework import serializers
from adminApp.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"

