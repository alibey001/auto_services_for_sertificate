from django.contrib import admin
from .models import  *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number' , 'address')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Cassa)
admin.site.register(Garaj)
admin.site.register(Profession)
admin.site.register(Report)
admin.site.register(Comment)
admin.site.register(Attendence)