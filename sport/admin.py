from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Program)


@admin.register(Day)
class DayInline(admin.ModelAdmin):
    model = Day
    extra = 0
    ordering = ('-program',)


admin.site.register(Exercise)