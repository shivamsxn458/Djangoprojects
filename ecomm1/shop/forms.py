from django import forms
from django.forms import ModelForm
from .models import PurchaseEnquiry, SellEnquiry ,AllProductNames
from django.forms.widgets import TextInput, Textarea, FileInput

# -------------------------------------------------------------------

class CustomerForm(ModelForm):

	username = forms.CharField(widget=forms.HiddenInput())
	Status = forms.CharField(widget=forms.HiddenInput())


	# def __init__(self, *args, **kwargs):
	# 	super(PurchaseEnquiryForm, self).__init__(*args, **kwargs)
	# 	for field_name, field in self.fields.items():
	# 		# if isinstance(field.widget, Textarea):
	# 			field.widget.attrs.update({
	# 				# 'placeholder': '',
	# 				'multiple': False,
	# 				'class': 'form-control',
	# 				'style': 'display: inline-block; width: auto; height: auto; margin: auto; padding: 1px; border: none; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); font-size: 16px; font-weight: 400; color: #333; background-color: #fff;',
	# 			})


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].initial = self.instance.username
		self.fields['username'].label = ''
		self.fields['Status'].initial = self.instance.Status
		self.fields['Status'].label = ''


	class Meta:
		model = PurchaseEnquiry
		fields = '__all__'

# -------------------------------------------------------------------

class SellEnquiryForm(ModelForm):


	dropdown_field = forms.ChoiceField(choices=[], required=False ,widget=forms.HiddenInput())
	username = forms.CharField(widget=forms.HiddenInput())
	Status = forms.CharField(widget=forms.HiddenInput())


	def __init__(self, *args, **kwargs):
		super(SellEnquiryForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			# if isinstance(field.widget, Textarea):
				field.widget.attrs.update({
					# 'placeholder': '',
					'multiple': False,
					'class': 'form-control',
					'style': 'display: inline-block; width: auto; height: auto; margin: auto; padding: 1px; border: none; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); font-size: 16px; font-weight: 400; color: #333; background-color: #fff;',
				})
			# else:
			# 	field.widget.attrs.update({'multiple': True, 'class': 'form-control', 'style': 'width:auto; margin: 0 auto;'})



	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['dropdown_field'].choices = instance.get_dropdown_choices()
			self.fields['dropdown_field'].label = ''
		else:
			self.fields['dropdown_field'].choices = []
			self.fields['dropdown_field'].label = ''


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].initial = self.instance.username
		self.fields['username'].label = ''
		self.fields['Status'].initial = self.instance.Status
		self.fields['Status'].label = ''

	class Meta:
		model = SellEnquiry
		fields = '__all__'




	# fields = ['First_name',  ]

# -------------------------------------------------------------------

