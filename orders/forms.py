from django import forms
from .models import Order


PAYMENT_CHOICES = (
    ("cash", "Наличными"),
    ("card_online", "Картой онлайн"),
    ("card_courier", "Картой курьеру"),
)

DELIVERY_CHOICES = (
    ("pick_up_point", "Пункт выдачи"),
    ("delivery", "Курьерская доставка"),
    ("mail", "Почта России"),
    ("cdek", "СДЭК"),
)


class QuickOrderForm(forms.Form):
    name = forms.CharField(max_length=50, label="Имя")
    last_name = forms.CharField(max_length=50, label="Фамилия")
    email = forms.EmailField(label="Эл.почта")
    phone = forms.CharField(max_length=50, label="Телефон")
    payment = forms.ChoiceField(choices=PAYMENT_CHOICES, label='Способ оплаты')
    delivery = forms.ChoiceField(choices=DELIVERY_CHOICES, label='Способ Доставки')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('name', 'last_name', 'email', 'phone')