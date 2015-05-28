from linkyou_widget.models import Widget
from mezzanine import template

register = template.Library()

@register.as_tag
def widget_list(*args):

    widgets = Widget.objects.all()
    return list(widgets) 
