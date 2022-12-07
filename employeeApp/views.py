from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from employeeApp.models import LeaveApplication
from employeeApp.serializers import LeaveSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def leaveApi(request,id=0):
    if request.method=='GET':
        leave = LeaveApplication.objects.all()
        leave_serializer = LeaveSerializer( leave, many=True)
        return JsonResponse(leave_serializer.data, safe=False)

    elif request.method=='POST':
        leave_data=JSONParser().parse(request)
        leave_serializer = LeaveSerializer(data= leave_data)
        if leave_serializer.is_valid():
            leave_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        leave_data = JSONParser().parse(request)
        leave=LeaveApplication.objects.get(id= leave_data['id'])
        leave_serializer=LeaveSerializer( leave,data= leave_data)
        if  leave_serializer.is_valid():
            leave_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        leave=LeaveApplication.objects.get(id=id)
        leave.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)