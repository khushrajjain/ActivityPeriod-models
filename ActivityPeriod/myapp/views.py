from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize
import json
import pytz,random
from faker import Faker # package to generate Random data
from datetime import datetime  
from datetime import timedelta 

# Returns the JSON of all the members and their Activity Periods
def home(request):
    users = User.objects.all()
    members=[]
    for user in users:
        print(user.u_id)
        data = {}
        activity_val = []
        
        data["id"] = user.u_id
        data["real_name"] = user.real_name
        data["tz"] = str(user.tz)
        
        # get all the activity period of current user
        for activity in UserActivity.objects.filter(u_id = user.u_id):
            activity_val.append({
                'start_time':activity.start_time.strftime("%b %d %Y %I:%M%p"),
                'end_time':activity.end_time.strftime("%b %d %Y %I:%M%p")})
        
        data["activity_periods"] = activity_val
        members.append(data)
        
    user_activity = {"ok":True,"members":members}
    data = {
        "json":json.dumps(user_activity,indent=4)
    }
        
    return render(request, "activity.html",data)


# Generating Random Users
def generateuser(request):
    faker = Faker() # facker Object for creating random data
    User.objects.create(real_name = faker.name(),tz = faker.timezone())
        
    return render(request, "generateuser.html",{"name":"user"})


# Generate Activity For Random User
def generateactivity(request):
    rand_user = User.objects.order_by("?").first()
    # Insert Dummy activity period in database
    UserActivity.objects.create(u_id = rand_user,
                                start_time=datetime.now(),
                                end_time=datetime.now() + timedelta(days=random.randrange(0,1),minutes=random.randrange(10,100)) )
    
    return render(request, "generateactivity.html",{"name":rand_user.real_name})
    
