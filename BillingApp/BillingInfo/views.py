from django.shortcuts import render
from django.views import View
from BillingInfo.models import BillInfo
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class AddBillingPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_billing.html')

    def post(self, request):
        content = request.POST['content']
        amount = request.POST['amount']
        event_time = datetime.datetime.now()

        bill_info = BillInfo(content=content,
                             amount=amount,
                             event_time=event_time,
                             owner=request.user)
        bill_info.save()

        return HttpResponseRedirect("/test_show_all/")

def DeleteBilling(request, id):
    deleted_bill = BillInfo.objects.get(id=id)
    deleted_bill.delete()
    return HttpResponseRedirect("/test_show_all/")

@login_required
def test_show_all(request):
    billing_list = BillInfo.objects.filter(
        owner=request.user).order_by('-event_time')
    return render(request, 'test_show_all.html', {
        'billing_list': billing_list})