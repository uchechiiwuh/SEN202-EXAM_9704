from django.contrib import admin
from .models import Manager, Intern, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_address', 'city', 'state', 'country', 'is_primary']
    list_filter = ['city', 'state', 'country', 'is_primary']
    search_fields = ['street_address', 'city', 'state']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Address Details', {
            'fields': ('street_address', 'city', 'state', 'postal_code', 'country')
        }),
        ('Settings', {
            'fields': ('is_primary',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'department', 'has_company_card', 'is_active']
    list_filter = ['department', 'has_company_card', 'is_active', 'hire_date']
    search_fields = ['first_name', 'last_name', 'email', 'department']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Employment Details', {
            'fields': ('hire_date', 'salary', 'department', 'has_company_card', 'is_active')
        }),
        ('Address', {
            'fields': ('address',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mentor', 'internship_end', 'is_active']
    list_filter = ['mentor', 'is_active', 'hire_date', 'internship_end']
    search_fields = ['first_name', 'last_name', 'email', 'mentor__first_name', 'mentor__last_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Employment Details', {
            'fields': ('hire_date', 'salary', 'is_active')
        }),
        ('Internship Information', {
            'fields': ('mentor', 'internship_end')
        }),
        ('Address', {
            'fields': ('address',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
