from django.contrib import admin

from .models import Case, Machine, Problem

admin.site.register(Case)
admin.site.register(Machine)
admin.site.register(Problem)