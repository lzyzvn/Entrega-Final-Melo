from django import forms
class LoginFormulario(forms.Form):
  nombre = forms.CharField()
  contraseña= forms.CharField()
  email= forms.CharField()