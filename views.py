from django.shortcuts import render
from linkyou_widget.models import Widget

# Create your views here.

def widget_view(request):
     widget_list = Widget.objects.all()
     context = {'widget_list' : widget_list}
     return render(request, 'widget/widget.html', context)
