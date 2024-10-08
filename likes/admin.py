from django.contrib import admin
from .models import Like

# Register your models here.


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet", "created_at")
    search_fields = ("user__username",)
    list_filter = ("created_at",)
