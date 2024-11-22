from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(
		attrs= {
			'placeholder': 'Add your task...',
			'required':'required',
			'id':'task',
		}
	))
	
	class Meta:
		model = Task
		fields = ['title']