from django.shortcuts import render
from .models import ClassicPerformance

def classic_list(request):
    performances = ClassicPerformance.objects.all().order_by('date')
    return render(request, 'classic/classic_list.html', {'performances': performances})
