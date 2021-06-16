from django.contrib import admin
from .models import Customer


class UmbrellaAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'join_date', 'city', 'notification_time', 'active_user')
    search_fields = ("chat_id",)
    list_filter = ("join_date",)
    empty_value_display = "-пусто-"

admin.site.register(Customer, UmbrellaAdmin)
