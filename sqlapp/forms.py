from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'mail', 'gender', 'sns_acount']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'mail': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
			'gender': forms.Select(attrs={'class': 'form-control form-control-sm'}),
			'sns_acount': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
		}

		# gender フィールドに選択肢を提供する場合
		GENDER_CHOICES = [
			('male', 'Male'),
			('female', 'Female'),
			('other', 'Other'),
		]

		gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-text'}))