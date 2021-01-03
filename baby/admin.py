from django.contrib import admin
from baby.models import Baby


@admin.register(Baby)
class BabyAdmin(admin.ModelAdmin):
    pass
