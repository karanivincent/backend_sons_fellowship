from django.contrib import admin
from .models import Members, Pledge, Attendance, Campaign

admin.site.site_header = 'Sons Fellowship'


# class CustomAdmin(admin.ModelAdmin):
    # fields= ('time',)
    # exclude = ('time',)
    # list_display = ('nameType', 'name')
    # list_filter = ('name', 'time')

class AttendanceDisplay(admin.ModelAdmin):
    list_display = ('member', 'seat_no', 'date')

admin.site.register(Members)
admin.site.register(Pledge)
admin.site.register(Attendance, AttendanceDisplay)
admin.site.register(Campaign)