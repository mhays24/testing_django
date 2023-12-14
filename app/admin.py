from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import School, Membership

class MembershipInline(admin.StackedInline):
    model = Membership
    can_delete = False
    verbose_name_plural = 'membership'

class UserAdmin(BaseUserAdmin):
    inlines = (MembershipInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(School)