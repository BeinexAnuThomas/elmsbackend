# from django.conf.urls import url
from adminApp import views
from django.urls import re_path
# from django.conf.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # url(r'^department/$',views.departmentApi),
    # url(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee/$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),
    re_path(r'^employeebyid/([0-9]+)$',views.employeebyid),
    

    re_path(r'^SaveFile$', views.SaveFile)
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

