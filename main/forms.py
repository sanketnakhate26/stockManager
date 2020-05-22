from django.forms import ModelForm
from .models import Overview

class OverviewForm(ModelForm):
    class Meta:
        model = Overview
        fields = '__all__'
