from django.urls import path
from . import views

app_name = "hospitals"

urlpatterns = [
    path("hospitalList", views.HospitalDetailedList.as_view(), name="hospital_list"),
    path("hospitalDetail", views.HospitalDetailedSingle.as_view(), name="hospital_read"),

]