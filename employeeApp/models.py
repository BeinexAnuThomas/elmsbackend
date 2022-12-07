from django.db import models
from adminApp.models import Employees
# Create your models here.


class LeaveApplication(models.Model):
    user=models.ForeignKey(Employees, on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now=False, auto_now_add=True,editable=False)
    nature_of_leave = models.CharField(max_length=100)
    first_Day = models.DateField()
    last_Day = models.DateField()
    number_Of_Days = models.IntegerField()
    status = models.CharField(max_length=12,default='pending') #pending,approved,rejected,cancelled
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name='Leave'
        verbose_name_plural='Leaves'
        ordering=['apply_date']


    def __str__(self):
        return '{0} '.format(self.nature_of_leave)

