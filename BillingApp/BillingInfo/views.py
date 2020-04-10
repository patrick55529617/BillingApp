from django.shortcuts import render
from django.views import View
from BillingInfo.models import BillInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.urls import reverse

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

        return HttpResponseRedirect(reverse('test_show_all'))

def DeleteBilling(request):
    check_box_list = request.POST.getlist("check_box_list")
    for deleted_index in check_box_list:
        deleted_bill = BillInfo.objects.get(id=deleted_index)
        deleted_bill.delete()
    return HttpResponseRedirect(reverse('test_show_all'))

class BillingListPage(LoginRequiredMixin, View):
    def get(self, request):
        billing_list = BillInfo.objects.filter(
            owner=request.user).order_by('-event_time')
        if request.GET.get('date'):
            date = datetime.strptime(date, "%m/%d/%Y").date()
            billing_list = billing_list.filter(date=date)
        return render(request, 'test_show_all.html', {
            'billing_list': billing_list})