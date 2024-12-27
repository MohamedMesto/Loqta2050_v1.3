from django.contrib import admin
from .models import Aboutus
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Aboutus)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)