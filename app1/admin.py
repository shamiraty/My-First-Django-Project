from django.contrib import admin
from . import models

class SlideShowAdmin(admin.ModelAdmin):
    list_per_page=7
    list_max_show_all=5
    list_display=('Title','Heading','RegisteredDate','image_tag')
admin.site.register(models.SlideShow,SlideShowAdmin)
