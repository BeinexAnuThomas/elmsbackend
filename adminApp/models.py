from django.db import models

# Create your models here.
# BLOOD_GRPS = (
#     ("A+", "A+"),
#     ("A-", "A-"),
#     ("B+", "B+"),
#     ("B-", "B-"),
#     ("O+", "O+"),
#     ("O-", "O-"),
#     ("AB+","AB+"),
#     ("AB-", "AB-"),
# )
# MARTIAL_STS = (
#     ("SINGLE", "SINGLE"),
#     ("MARRIED", "MARRIED"),
#     ("DIVORCED", "DIVORCED")
# )    
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    employee_Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_Number = models.IntegerField()
    emergency_Contact_Number = models.IntegerField()
    address = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    dOB = models.DateField()
    martial_Status = models.CharField(max_length=100)
    blood_Group = models.CharField(max_length=100)
    # # martial_Status = models.CharField(max_length = 20, choices = MARTIAL_STS, default = '')
    # # blood_Group = models.CharField(max_length = 20, choices = BLOOD_GRPS, default = '')
    job_Title = models.CharField(max_length=100)
    work_Location = models.CharField(max_length=100)
    date_Of_Joining = models.DateField()
    reporting_To = models.CharField(max_length=100)
    linkedin_Link =  models.URLField(max_length=300)
    Photo_File_Name = models.CharField(max_length=100)