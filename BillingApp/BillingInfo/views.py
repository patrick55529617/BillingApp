from django.shortcuts import render
from django.views import View
from BillingInfo.models import BillInfo
from django.http import HttpResponse, HttpResponseRedirect
import datetime

class AddBillingPage(View):
    def get(self, request):
        return render(request, 'add_billing.html')

    def post(self, request):
        bill_content = request.POST['bill_content']
        cost = request.POST['cost']
        bill_release_date = datetime.datetime.now()

        bill_info = BillInfo(bill_content = bill_content, cost = cost, bill_release_date = bill_release_date)
        bill_info.save()

        return HttpResponseRedirect("/test_show_all/")

def test_show_all(request):
    billing_list = BillInfo.objects.all().order_by('-bill_release_date')
    return render(request, 'test_show_all.html', {'billing_list':billing_list})