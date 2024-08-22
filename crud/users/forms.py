from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'active']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        # Extract the 'edit' keyword argument
        edit = kwargs.pop('edit', False)
        super().__init__(*args, **kwargs)
        
        # If 'edit' is True, remove the password field
        if edit:
            self.fields.pop('password')
