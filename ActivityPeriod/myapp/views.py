from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize
import json
import pytz,random
from faker import Faker
from datetime import datetime  
from datetime import timedelta 


def home(request):
    users = User.objects.all()
    members=[]
    for user in users:
        data = {}
        print(user.u_id)
        data["id"] = user.u_id
        data["real_name"] = user.real_name
        data["tz"] = str(user.tz)
        activity_val = []
        for activity in UserActivity.objects.filter(u_id = user.u_id):
            activity_val.append({
                'start_time':activity.start_time.strftime("%b %d %Y %I:%M%p"),
                'end_time':activity.end_time.strftime("%b %d %Y %I:%M%p")})
        data["activity_periods"] = activity_val
        members.append(data)
        
    user_activity = {"ok":True,"members":members}
        
    return HttpResponse(json.dumps(user_activity), content_type='application/json')



def generateuser(request):
    faker = Faker()
    User.objects.create(real_name = faker.name(),tz = faker.timezone())
        
    return HttpResponse("New User Generated generated sucessfully go Back and refresh to see new Json")



def generateactivity(request):
    rand_user = User.objects.order_by("?").first()
    UserActivity.objects.create(u_id = rand_user,
                                start_time=datetime.now(),
                                end_time=datetime.now() + timedelta(days=random.randrange(0,1),minutes=random.randrange(10,100)) )
    
    return HttpResponse("Activity Period Generated sucessfully for => " + rand_user.real_name +" <=go Back to see new Json")
    
