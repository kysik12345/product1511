from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class SignForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Номер телефона какого-то формата')

    # def clean_password(self):
    #     cleaned_data = self.cleaned_data
    #     if cleaned_data['password'] != cleaned_data['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')
    #     return cleaned_data['password2']

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'email', 'password1', 'password2')



# class CustomPasswordChangeForm(forms.Form):
#     old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
#     new_password_1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
#     new_password_2 = forms.CharField(label="Повторите новый пароль", widget=forms.PasswordInput)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         new_password_1 = cleaned_data['new_password_1']
#         new_password_2 = cleaned_data['new_password_2']
#         old_password = cleaned_data['old_password']
#
#         if new_password_1 and new_password_2 and new_password_1 != new_password_2:
#             raise forms.ValidationError("Пароли не совпадают!")
#
#         if new_password_1 and new_password_2 and new_password_1 == new_password_2 and new_password_1 == old_password:
#             raise forms.ValidationError("Пароль совпадает с текущийм")
#
#         return cleaned_data

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Старый пароль')
    new_password = forms.CharField(widget=forms.PasswordInput, label='Новый пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Подтверждение нового пароля')

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        # Проверка на совпадение нового пароля со старым
        if old_password == new_password:
            self.add_error('new_password', 'Новый пароль не должен совпадать со старым.')

        # Проверка на совпадение нового пароля с подтверждением
        if new_password != confirm_password:
            self.add_error('confirm_password', 'Пароли не совпадают.')

        return cleaned_data

    
