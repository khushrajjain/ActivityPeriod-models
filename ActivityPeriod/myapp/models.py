from django.db import models
import pytz
from timezone_field import TimeZoneField



# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = TimeZoneField()
    
   
    
class UserActivity(models.Model):
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    