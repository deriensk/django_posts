from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'title',
			'image',
			'content',
			'draft',
			'email',
			'publish'
			]

	def clean_title(self):
		title = self.cleaned_data.get('title')
		if len(title) < 5:
			raise forms.ValidationError('The title length must be more then 3 characters')
		return title	

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not extension == 'com':
			raise forms.ValidationError('Please provide a valid .com email.')
		return email			