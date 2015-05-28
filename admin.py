from django.contrib import admin
from linkyou_widget.models import Widget

# Register your models here.

class WidgetAdmin(admin.ModelAdmin):

     list_display = ('title', 'content', 'show_in_widget')

admin.site.register(Widget, WidgetAdmin)
