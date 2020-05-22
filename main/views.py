from django.http import HttpResponse
from django.shortcuts import render
from .models import Overview
from .forms import OverviewForm

def overview(request):
    all_overview = Overview.objects.all()
    # context = {'all_overview': all_overview}
    form = OverviewForm()
    if request.method == 'POST':
        print(request.POST)
        form = OverviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = OverviewForm()
    context = {'form': form,'all_overview': all_overview}
    return render(request,'main/overview.html',context)

def addstock(request):
    form = OverviewForm()
    if request.method == 'POST':
        print(request.POST)
        form = OverviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = OverviewForm()
    context_addstock = {'form': form}
    return render(request,'main/addstock.html',context_addstock)