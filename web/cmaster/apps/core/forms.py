from django import forms


class RequestForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"})
    )
    phone = forms.CharField(
        max_length=20,
        label="Телефон",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "+7 (___) ___-__-__"})
    )
    email = forms.EmailField(
        max_length=254,
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "example@mail.ru"})
    )
    device_type = forms.ChoiceField(
        label="Тип устройства",
        choices=[],
        widget=forms.Select(attrs={"class": "form-select"})
    )
    service = forms.ChoiceField(
        label="Услуга",
        choices=[],
        widget=forms.Select(attrs={"class": "form-select"})
    )
    problem_description = forms.CharField(
        label="Описание проблемы",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Опишите, что случилось..."})
    )
    is_pickup = forms.BooleanField(
        label="Нужен выезд мастера",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    address = forms.CharField(
        max_length=255,
        label="Адрес для выезда",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Улица, дом, квартира"})
    )
