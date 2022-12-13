from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
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


def leaves_pending_list(request):
	leave= LeaveApplication.objects.filter(status="pending")
	leave_serializer = LeaveSerializer( leave, many=True)
	return JsonResponse(leave_serializer.data, safe=False)



def leaves_approved_list(request):
	leave= LeaveApplication.objects.filter(status="approve")
	leave_serializer = LeaveSerializer( leave, many=True)
	return JsonResponse(leave_serializer.data, safe=False)

def leaves_rejected_list(request):
	leave= LeaveApplication.objects.filter(status="reject")
	leave_serializer = LeaveSerializer( leave, many=True)
	return JsonResponse(leave_serializer.data, safe=False)


@csrf_exempt
def leavebyuser(request,id=0):
    if request.method=='GET':
        leave = LeaveApplication.objects.filter(user=id)
        leave_serializer = LeaveSerializer( leave, many=True)
        return JsonResponse(leave_serializer.data, safe=False)

# @api_view(['GET', 'PATCH', 'DELETE'])
# def approveupdate(self,request,*args,**kwargs):
#     leave = LeaveApplication.objects.get()
#     data = request.data
#     leave.status ="approved"
#     leave.save()
#     leave_serializer = LeaveSerializer(leave)
#     return JsonResponse(leave_serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
# get by id
def leavebyid(request,id):
    try: 
        leave = LeaveApplication.objects.get(id=id) 
    except LeaveApplication.DoesNotExist: 
        return JsonResponse({'message': 'The id does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        leave_serializer = LeaveSerializer(leave) 
    return JsonResponse(leave_serializer.data)
     


# @csrf_exempt
# def approveupdate(request,id=0):
#     if request.method=='PUT':
#         leave_data = JSONParser().parse(request)
#         leave=LeaveApplication.objects.get(id=id)
#         leave_serializer=LeaveSerializer(leave,data= leave_data)
#         leave_serializer.status='approve'
#         print(leave_serializer.status)
#         # if  leave_serializer.is_valid():
#         #     print(leave_serializer.status)
#         #     leave_serializer.save()
#         return JsonResponse("Leave Approved !!!", safe=False)
#         # print(leave_serializer.status)
#         # return JsonResponse("Failed to approve.", safe=False)

@csrf_exempt
def approveupdate(request,id=0):
    if request.method=='PUT':
        leave=LeaveApplication.objects.get(id=id)
        leave.status='approve'
        # if leave.is_valid():
        leave.save()
        return JsonResponse("Leave Approved !!!", safe=False)
        # return JsonResponse("Failed to approve !!!", safe=False)

    # # leave.status='approve'
    # leave_serializer.save()
    # return JsonResponse("Leave Approved !!!" , safe=False)

@csrf_exempt
def rejectupdate(request,id=0):
    if request.method=='PUT':
        leave=LeaveApplication.objects.get(id=id)
        leave.status='reject'
        # if leave.is_valid():
        leave.save()
        return JsonResponse("Leave Rejected !!!", safe=False)

# @csrf_exempt
# def rejectupdate(request,id):
#     leave=LeaveApplication.objects.get(id=id)
#     leave_serializer=LeaveSerializer(data = leave_data)
#     leave_serializer.status='reject'
#     if  leave_serializer.is_valid():
#         leave_serializer.save()
#         return JsonResponse("Leave Rejected !!!", safe=False)
#     return JsonResponse("Failed to reject.", safe=False)
#     # # leave.status='approve'
#     # leave_serializer.save()
#     # return JsonResponse("Leave Rejected !!!" , safe=False)