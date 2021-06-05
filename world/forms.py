from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'lt', 'lg', 'content')

		widgets = {
			'author': forms.TextInput(attrs={'value':'', 'id':'writer', 'type':'hidden'}),
			'lt':forms.NumberInput(attrs={'value':'', 'id':'lat', 'type':'hidden'}),
			'lg':forms.NumberInput(attrs={'value':'', 'id':'long', 'type':'hidden'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'What is here?'})
		}

		labels = {
			'author':_(''),
			'lt':_(''),
			'lg':_(''),
			'content':_('')
		}