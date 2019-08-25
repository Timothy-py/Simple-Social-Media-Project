from django.contrib import admin
from Groups.models import Group, GroupMember

# Register your models here.

class GroupMemberInline(admin.TabularInline):   # *****
    model = models.GroupMember

admin.site.register(Group)
