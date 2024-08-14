from django.core import validators
from django import forms 
from .models import OfferTable

from stuff_panel.models import Notification,Pointaddmodel

class Massage(forms.ModelForm):
    class Meta:
        model = OfferTable
        fields = ['offer_name', 'duration_date']
        widgets={
            'offer_name': forms.TextInput(attrs={'class':'form-control'}),
            'duration_date': forms.TextInput(attrs={'class':'form-control'}),
            
        }
        


class notificationform(forms.ModelForm):
    class Meta:
        model=Notification
        fields=['givenotification']
        
        
class pointaddform(forms.ModelForm):
    class Meta:
        model=Pointaddmodel
        fields=['email','pointno']
        