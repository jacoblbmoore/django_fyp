from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from venues.models import Section, Table


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    venue_name = forms.CharField(required=True, label="Venue Name")
    venue_address = forms.CharField(required=True, label="Venue Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'venue_name', 'venue_address', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['password2'].widget.attrs['autocomplete'] = 'new-password'

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Account'))

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        self.validate_password(password1)
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters.")

        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least 1 number.")

        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least 1 uppercase letter.")

        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least 1 lowercase letter.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must contain at least 1 special character.")


class UsernameAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            return username.lower()


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'booking_priority']


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'min_seats', 'max_seats']

