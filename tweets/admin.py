from django.contrib import admin
from .models import Tweet


class ContainsElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk 포함 여부"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Elon Musk 포함"),
            ("no", "Elon Musk 미포함"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(content__icontains="Elon Musk")
        if self.value() == "no":
            return queryset.exclude(content__icontains="Elon Musk")


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_at")
    search_fields = ("content", "user__username")
    list_filter = ("created_at", ContainsElonMuskFilter)
