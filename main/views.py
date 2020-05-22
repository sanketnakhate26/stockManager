from django.http import HttpResponse
from django.shortcuts import render
from main.models import Overview
from main.models import History
from .forms import OverviewForm
from django.db.models import Sum

def overview(request):
    all_overview = Overview.objects.all()
    # context = {'all_overview': all_overview}
    form = OverviewForm()
    if request.method == 'POST':
        if 'create_post' in request.POST:
            print(request.POST)
            form = OverviewForm(request.POST)
            if form.is_valid():
                form.save()
                form = OverviewForm()
        if 'update_post' in request.POST:
            data_test = {}
            # print('update post')
            print(request.POST)
        if 'delete_post' in request.POST:
            target_id = request.POST['stock_id']
            sellprice = request.POST['sell_stock']
            instance = Overview.objects.get(id=target_id)

            record = History(name=instance.name, quantity=instance.quantity, buy_price=float(instance.buy_price), sell_price=float(sellprice), trade_type=instance.trade_type, date_buy=instance.date_buy, profit_loss=(float(sellprice)-float(instance.buy_price)))
            record.save()
            instance.delete()
    context = {'form': form,'all_overview': all_overview}
    return render(request,'main/overview.html',context)

def history(request):
    data = History.objects.all()
    Total_profit_loss = History.objects.aggregate(Sum('profit_loss'))['profit_loss__sum']
    print(Total_profit_loss)
    context = {'data': data, 'Total_profit_loss': Total_profit_loss}
    return render(request,'main/history.html',context)