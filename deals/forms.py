import csv
from django import forms
# from django.contrib.auth import

from .models import Deals


class DataForm(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f = self.cleaned_data['data_file'].file
        reader = csv.DictReader(f)

        for deal in reader:
            Deals.objects.create(
                customer=['customer'], item=['item'],
                total=['total'], quantity=['quantity'],
                date=['date'])
