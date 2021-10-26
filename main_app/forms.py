from django.forms import ModelForm
from .models import Swimming

class SwimmingForm(ModelForm):
    class Meta:
        model = Swimming
        fields = ['date', 'time']