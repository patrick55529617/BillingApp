from BillingInfo.models import BillInfo
from BillingInfo.forms import BillInfoForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.generic.base import TemplateResponseMixin
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
import datetime


class AddBillingPage(View):
    def get(self, request):
        return render(request, 'add_billing.html')

    def post(self, request):
        content = request.POST['content']
        amount = request.POST['amount']
        event_time = datetime.datetime.now()

        bill_info = BillInfo(content=content,
                             amount=amount,
                             event_time=event_time)
        bill_info.save()

        return HttpResponseRedirect("/test_show_all/")


class BillingDetailPage(TemplateResponseMixin, View):
    template_name = 'billing_detail.html'

    def get(self, request, billing_id):
        bill_info = BillInfo.objects.get(id=billing_id)
        form = BillInfoForm(instance=bill_info)
        return self.render_to_response({
            'billing_id': billing_id,
            'form': form
        })

    def post(self, request, billing_id):
        bill_info = BillInfo.objects.get(id=billing_id)
        form = BillInfoForm(request.POST, instance=bill_info)

        if form.is_valid():
            form.save()
            return redirect(reverse('test_show_all'))

        return self.render_to_response({'form': form})


def test_show_all(request):
    billing_list = BillInfo.objects.all().order_by('-event_time')
    return render(request, 'test_show_all.html', {
        'billing_list': billing_list})
