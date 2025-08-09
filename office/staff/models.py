from django.db import models

# Create your models here.


class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name   


class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default = 0)
    bonus = models.IntegerField(default = 0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_hire =models.DateField()
    phone = models.IntegerField(default = 0)
    

    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.dept)