from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django import forms
from croppie.fields import CroppieField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div
from .models import Doctor, AllUser, Teacher, Student

class AllUserUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = AllUser
        fields = ("first_name", 'id_number', "gender","user_type", "last_name", "username", "email")
        field_classes = {'username': UsernameField}
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('user_type'), Column('gender')),
            Row(Column('id_number')),
            Row(Column('first_name'), Column('last_name')),
            Row(Column('username'), Column('email')),
            Row(Column('password1'), Column('password2')),
            Div(Submit('submit', 'Submit', css_class='btn col-4 btn-success'), css_class="col-12 d-flex justify-content-center"),

        )    

class DateInput(forms.DateInput):
    input_type = 'date'

class DoctorUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    photo = CroppieField(
        options={

            'viewport': {
                'width': 150,
                'height': 150,
            },
            'boundary': {
                'width': 160,
                'height': 160,
            },
            'showZoomer': True,
        },
        required=False,

    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = Doctor
        fields = (
            "first_name","last_name",
            "username", "email",
            "gender", "phone", "emergency_contact_number",
            "password1", "password2", "photo", "current_address", "permanent_address", "note"
        )
        field_classes = {
            'username': UsernameField,
        }
        widgets = {
            'gender': forms.Select(
                attrs={'class': 'form-select select2'}
            ),
            'current_address': forms.Textarea(
                attrs={'rows': '2'}
            ),
            'permanent_address': forms.Textarea(
                attrs={'rows': '2'}
            ),
            'note': forms.Textarea(
                attrs={'rows': '2'}
            ),
        }

class DoctorUserChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    photo = CroppieField(
        options={

            'viewport': {
                'width': 150,
                'height': 150,
            },
            'boundary': {
                'width': 160,
                'height': 160,
            },
            'showZoomer': True,
        },
        required=False,

    )

    class Meta:
        model = AllUser
        fields = (
            "first_name", "last_name",
            "username", "email",
            'gender','phone', 'emergency_contact_number',
            'photo', 'current_address', 'permanent_address',
            'note',
        )
        field_classes = {
            'username': UsernameField,
        }
        widgets = {
            'gender': forms.Select(
                attrs={'class': 'form-select select2'}
            ),
            'current_address': forms.Textarea(
                attrs={'rows': '2'}
            ),
            'permanent_address': forms.Textarea(
                attrs={'rows': '2'}
            ),
            'note': forms.Textarea(
                attrs={'rows': '2'}
            ),
        }

class TeacherUserCreationForm(DoctorUserCreationForm):
    class Meta(DoctorUserCreationForm.Meta):
        model = Teacher

class TeacherUserChangeForm(DoctorUserChangeForm):
    class Meta(DoctorUserChangeForm.Meta):
        model = Teacher

class StudentUserCreationForm(DoctorUserCreationForm):
    class Meta(DoctorUserCreationForm.Meta):
        model = Student
        
class StudentUserChangeForm(DoctorUserChangeForm):
    class Meta(DoctorUserChangeForm.Meta):
        model = Student