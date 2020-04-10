from django.forms import ModelForm
from BillingInfo.models import BillInfo


class BillInfoForm(ModelForm):

    class Meta:
        model = BillInfo
        fields = ['content', 'amount', 'event_time']
