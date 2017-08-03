from django import forms
from bookaddress.models import Contact


# https://docs.djangoproject.com/en/1.11/topics/forms/
class LoginForm(forms.Form):
    user = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))


# En este caso, heredamos desde ModelForm porque el formulario se crea directamente desde un modelo
# https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'email']
