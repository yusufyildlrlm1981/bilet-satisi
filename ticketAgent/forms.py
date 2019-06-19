from django import forms
from .models import *


class LogInForm(forms.ModelForm):
    class Meta:
        model = LogIn
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('Parola')
        return password


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['name', 'surname', 'email', 'password', 'repeat_password']
        widgets = {
            'Parola': forms.PasswordInput(),
            'Tekrar girin': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('Adý')
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('Soyadý')
        return surname

    def clean_password(self):
        password = self.cleaned_data.get('Parola')
        return password

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("Parola")
        confirm_password = cleaned_data.get("Tekrar girin")

        if password != confirm_password:
            raise forms.ValidationError(
                "Parola Uyuþmazlýgý"
            )

   

EVENTS = (
    ('', 'Etkinlikler Seç'),
    ('Tümü', 'Tümü'),
    ('Cinema', 'Cinema'),
    ('Theatre', 'Theatre'),
    ('Opera', 'Opera'),
    ('Dance', 'Dance'),
)

CITIES = (
    ('', 'Þehir Seç'),
    ('Tümü', 'Tümü'),
    ('Istanbul', 'Istanbul'),
    ('Izmir', 'Izmir'),
    ('Bursa', 'Bursa'),
    ('Trabzon', 'Trabzon'),
)

SHOWROOMS = (
    ('', 'Oda Seç'),
    ('Tümü', 'Tümü'),
    ('Jolly Joker Bursa', 'Jolly Joker Bursa'),
    ('Izmir Alsancak', 'Izmir Alsancak'),
    ('Kucuk Ciftlik Park', 'Kucuk Ciftlik Park'),
    ('Forum Trabzon', 'Forum Trabzon'),
)


class EventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['baturay'] = forms.ChoiceField(
            choices=EVENTS)


class CityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['my_choice_field'] = forms.ChoiceField(
            choices=CITIES)


class ShowroomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ShowroomForm, self).__init__(*args, **kwargs)
        self.fields['my_choice_field'] = forms.ChoiceField(
            choices=SHOWROOMS)
