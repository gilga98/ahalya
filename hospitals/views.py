from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HospitalDetailedList(APIView):
    
    def post(self, request, format=None):
        
        user_longitude = request.data["longitude"]
        user_latitude = request.data["latitude"]
        queryset = Hospital.objects.all()        
        serialized = HospitalSerializer(queryset, many=True,
        context={"user_longitude":user_longitude, "user_latitude":user_latitude}
        )

        return Response(serialized.data)


class HospitalDetailedSingle(APIView):

    def post(self, request, format=None):
        hospital_id = request.data["hospital_id"]
        user_longitude = request.data["longitude"]
        user_latitude = request.data["latitude"]
        queryset = Hospital.objects.get(id=hospital_id)

        serialized = HospitalSerializer(queryset, context={
           "user_longitude":user_longitude, "user_latitude":user_latitude
        })

        return Response(serialized.data)