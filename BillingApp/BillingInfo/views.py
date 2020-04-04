from django.shortcuts import render
from django.views import View
from BillingInfo.models import BillInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime

class AddBillingPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_billing.html')

    def post(self, request):
        content = request.POST['content']
        amount = request.POST['amount']
        event_time = datetime.now()

        bill_info = BillInfo(content=content,
                             amount=amount,
                             event_time=event_time,
                             owner=request.user)
        bill_info.save()

        return HttpResponseRedirect("/test_show_all/")

def DeleteBilling(request):
    check_box_list = request.POST.getlist("check_box_list")
    for deleted_index in check_box_list:
        deleted_bill = BillInfo.objects.get(id=deleted_index)
        deleted_bill.delete()
    return HttpResponseRedirect("/test_show_all/")

@login_required
def QueryOneDayRecord(request):
    one_date = datetime.strptime(request.POST['one_date'], "%m/%d/%Y").date()
    one_date_billing = BillInfo.objects.filter(
        event_time__date=one_date, owner=request.user)
    return render(request, 'query_one.html', {
        'billing_list': one_date_billing, 'date':one_date})

@login_required
def test_show_all(request):
    billing_list = BillInfo.objects.filter(
        owner=request.user).order_by('-event_time')
    return render(request, 'test_show_all.html', {
        'billing_list': billing_list})