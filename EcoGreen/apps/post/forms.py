from django import forms

from apps import post

from .models import post


class Formulario_alta_post(forms.ModelForm):
	

	class Meta:
		model = post
		fields = '__all__'