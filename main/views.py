from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plan
from .forms import PlanForm

def home(request):
    if request.method == "GET":
        all_plans = Plans.objects.all
        return render(request, 'home.html', {'all':all_plans})

    if request.method == "POST":
        # print(request.POST)
        form = PlanForm(request.POST or None)
        # print(dir(form), form.errors)

        if form.is_valid():
            form.save()
        return render(request, 'home.html')
    else: 
        return render(request, 'home.html')
def deletePlan(request):
    all_plans = Plans.objects.get(pk=id)
    all_plans.delete()
    return render(request, 'home.html')
    

    
    

    
    
