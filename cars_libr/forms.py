from django import forms  
from cars_libr.models import UserProfile  
  
  
class ProfileCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = ['age']