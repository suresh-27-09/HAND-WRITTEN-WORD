from django.db import models

# Create your models here.
class Register(models.Model):
          uname=models.CharField(max_length=30)
          roll=models.CharField(max_length=30)
          dept=models.CharField(max_length=30)
          password=models.CharField(max_length=30)
          phone=models.IntegerField()
          
          def __str__(self):
                    return self.uname
          
class Mark(models.Model):
          s_name=models.CharField(max_length=30)
          roll_no=models.CharField(max_length=30)
          mark=models.CharField(max_length=30)
          
          def __str__(self):
                    return self.s_name
