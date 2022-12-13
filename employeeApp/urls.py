# from django.conf.urls import url
from employeeApp import views
from django.urls import re_path,path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^empleave/$',views.leaveApi),
    re_path(r'^empleave/([0-9]+)$',views.leaveApi),
    path('empleave/pending/all/',views.leaves_pending_list,name='pendingleaveslist'),
    path('empleave/approved/all/',views.leaves_approved_list,name='approvedleaveslist'),
    path('empleave/rejected/all/',views.leaves_rejected_list,name='rejectedleaveslist'),
    re_path(r'^leavebyid/([0-9]+)$',views.leavebyid),
    re_path(r'^leavebyuser/([0-9]+)$',views.leavebyuser),
    re_path(r'^approveupdate/([0-9]+)$',views.approveupdate),
    re_path(r'^rejectupdate/([0-9]+)$',views.rejectupdate)
]