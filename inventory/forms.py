from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Product, AccountUser


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'expiration_date']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
