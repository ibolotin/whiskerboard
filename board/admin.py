from django.contrib import admin
from board.models import Category, Service, Status, Incident, Event
from tastypie.admin import ApiKeyInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]

admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Service, ServiceAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'severity')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Status, StatusAdmin)


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Incident, IncidentAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('start', 'service', 'incident', 'status', 'message')
    list_filter = ('service', 'incident', 'status')

admin.site.register(Event, EventAdmin)
