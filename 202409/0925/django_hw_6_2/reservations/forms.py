from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'Name',
                'maxlength': 10,
            }
        )
    )
    date = forms.DateField(required=False)
    
    class Meta:
        model = Reservation
        fields = '__all__'
        # exclude = ('title',)
