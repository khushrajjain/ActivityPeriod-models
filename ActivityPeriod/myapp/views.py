from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize
import json,jsonify


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
            activity_val.append({'start_time':str(activity.in_time),'end_time':str(activity.out_time)})
        data["activity_periods"] = activity_val
        members.append(data)
        
    user_activity = {"ok":True,"members":members}
        
    return HttpResponse(json.dumps(user_activity), content_type='application/json')
