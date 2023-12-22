from django import forms

class StudForm(forms.Form):
   s_name = forms.CharField(max_length=30)
   s_class = forms.CharField(max_length=30)
   s_addr = forms.CharField(max_length=30)
   s_school = forms.CharField(max_length=30)
   s_email = forms.EmailField(max_length=30)