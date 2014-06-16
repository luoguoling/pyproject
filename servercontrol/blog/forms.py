__author__ = 'Administrator'
from django.forms import ModelForm
from models import Blog
class AddForm(ModelForm):
    class Meta:
        model = Blog

