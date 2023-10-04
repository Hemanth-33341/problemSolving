from django.contrib import admin
from registration.models import form


# Register your models here.
@admin.register(form)
class FormAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "mail_ID"]
