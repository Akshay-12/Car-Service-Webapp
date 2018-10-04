from django import forms
from .models import Company
from .models import Cars

MY_CHOICES = []
post_company=Company.objects.all()
for i in post_company:
	MY_CHOICES.append([i.id,i.name])
print(MY_CHOICES)
class TheForm(forms.Form):
	#post_car=Cars.objects.all()
	name = forms.ChoiceField(label='Select your car company:',choices=MY_CHOICES,widget=forms.Select(attrs={'class':'custom-select mr-sm-2'}))
	'''car_model=forms.ChoiceField(label='Select car model:'),
	widget=forms.Select(choices=post_car)'''

MY_CHOICES_RE = []
post_car=Cars.objects.all()
for j in post_car:
	MY_CHOICES_RE.append([j.id,j.name])
print(MY_CHOICES_RE)
class TheFormRe(forms.Form):
	#post_car=Cars.objects.all()
	name = forms.ChoiceField(label='Select your car model:',choices=MY_CHOICES_RE,widget=forms.Select(attrs={'class':'custom-select mr-sm-2'}))