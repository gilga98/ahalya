from django.contrib import admin, messages
from .models import *
from django.contrib.auth.models import  Group, User
from import_export.admin import ImportExportModelAdmin
import datetime


admin.site.unregister(Group)
admin.site.unregister(User)
# Register your models here.
admin.site.site_header = "Ahalya"

admin.site.site_title = "Ahalya"

admin.site.index_title = "Hospital Administration"

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser: 
            obj.admitted_to = Hospital.objects.filter(admin=request.user)[0]
        super().save_model(request, obj, form, change)
        

    def get_queryset(self, request):
        qs = super(PatientAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admitted_to = Hospital.objects.filter(admin=request.user)[0])

    def discharge(self, request, queryset):

        queryset.update(discharged = True, discharge_timestamp=datetime.datetime.now())
        self.message_user(request, "Patients Discharged !")

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            print("Uhoh")
            self.exclude+=["admitted_to", "discharged", "discharge_timestamp"] #here!
        return super(PatientAdmin, self).get_form(request, obj, **kwargs)

    actions = ["discharge"]
    search_fields = ("name", "adhaar_number", "contact")

@admin.register(Hospital)
class HospitalAdmin(ImportExportModelAdmin):
    pass


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass