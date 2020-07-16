from rest_framework import serializers
from .models import *
from django.db.models import Count

from geopy.distance import geodesic

class HospitalSerializer(serializers.ModelSerializer):
    remaining_beds = serializers.SerializerMethodField("get_remaining_beds")
    geodesic_distance = serializers.SerializerMethodField("get_distance")
    bed_availability = serializers.SerializerMethodField("get_availability")
    comfortness = serializers.SerializerMethodField("get_comfortness")

    def get_remaining_beds(self, obj):
        return obj.total_beds - Patient.objects.filter(admitted_to=obj, discharged=False).count()

    def get_distance(self, obj):
        user_longitude = self.context.get("user_longitude")
        user_latitude = self.context.get("user_latitude")

        return round(geodesic((user_longitude, user_latitude), (obj.longitude, obj.latitude)).kilometers,2)

    def get_availability(self, obj):
        remaining_beds = obj.total_beds - Patient.objects.filter(admitted_to=obj, discharged=False).count()
        return int((remaining_beds/obj.total_beds)*100)
    
    def get_comfortness(self, obj):
        remaining_beds = obj.total_beds - Patient.objects.filter(admitted_to=obj, discharged=False).count()
        availability = int((remaining_beds/obj.total_beds)*100)
        user_longitude = self.context.get("user_longitude")
        user_latitude = self.context.get("user_latitude")

        distance = geodesic((user_longitude, user_latitude), (obj.longitude, obj.latitude)).miles
        
        comfortness = availability//distance

        return comfortness

    class Meta:
        model = Hospital
        fields = ["id","name", "logo","longitude", "latitude", "total_beds","address","pincode","phone_area_code","contact","country_code","comfortness","bed_availability", "remaining_beds", "geodesic_distance"]

