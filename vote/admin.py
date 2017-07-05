from django.contrib import admin

# Register your models here.
from vote.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
