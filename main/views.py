from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from main.models import Overview
from main.models import History
from .forms import OverviewForm
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import QueryDict


def calculateTax(price, type):
    tax = 0
    if type == "delivery":
        tax = price * 0.001063
        return tax
    else:
        if price > 40000:
            tax = 20 + price * 0.000085
            return tax
        else:
            tax = price * (0.000781)
            return tax

@login_required(login_url="/login/")
def overview(request):
    all_overview = Overview.objects.all()
    context = {'all_overview': all_overview}
    form = OverviewForm()
    if request.method == 'POST':
        if 'create_post' in request.POST:
            # new_instance = dict(request.POST)
            # new_instance['username']="admin"
            # form=QueryDict(new_instance)
            form = OverviewForm(request.POST)
            # form = new_instance
            if form.is_valid():
                form.save()
                form = OverviewForm()
        if 'update_post' in request.POST:
            data_test = {}
            # print('update post')
            print(request.POST)
        if 'sell_post' in request.POST:
            target_id = request.POST['stock_id']
            sellprice = request.POST['sell_stock']
            instance = Overview.objects.get(id=target_id)
            total_tax = calculateTax( (instance.buy_price + float(sellprice)), instance.trade_type)
            record = History(name=instance.name, quantity=instance.quantity, buy_price=float(instance.buy_price), sell_price=float(sellprice), trade_type=instance.trade_type, date_buy=instance.date_buy, tax=total_tax, profit_loss=((instance.quantity * (float(sellprice)-float(instance.buy_price)))- total_tax))
            record.save()
            instance.delete()
    context = {'form': form,'all_overview': all_overview}
    return render(request,'main/overview.html',context)

@login_required(login_url="/login/")
def history(request):
    data = History.objects.all()
    Total_profit_loss = History.objects.aggregate(Sum('profit_loss'))['profit_loss__sum']
    print(Total_profit_loss)
    context = {'data': data, 'Total_profit_loss': Total_profit_loss}
    return render(request,'main/history.html',context)

def user_login(request):
    context = {}
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect('/')
        else:
            context["error"]= "Provide Valid Credentials"
            return render(request,"auth/login.html",context)
    else:
        return render(request,"auth/login.html",context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

@login_required(login_url="/login/")
def user_logout(request):
    if request.method =="POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
