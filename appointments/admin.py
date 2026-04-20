from django.contrib import admin

# Register your models here.
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment_date', 'appointment_time', 'appointment_status', 'created_at')
    list_filter = ('appointment_status', 'appointment_date', 'doctor')
    search_fields = ('patient__name', 'doctor__name', 'reason')
    list_editable = ('appointment_status',)
    date_hierarchy = 'appointment_date'
    ordering = ('-appointment_date', '-appointment_time')
    fieldsets = (
        ('Patient & Doctor Information', {
            'fields': ('patient', 'doctor')
        }),
        ('Appointment Details', {
            'fields': ('appointment_date', 'appointment_time', 'appointment_status', 'reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')