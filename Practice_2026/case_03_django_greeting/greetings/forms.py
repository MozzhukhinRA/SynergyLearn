from django import forms
from .models import UserName


class UserNameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ["name"]
        labels = {"name": "Ваше имя"}
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите имя",
                    "autocomplete": "off",
                }
            )
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if not name:
            raise forms.ValidationError("Поле имени не должно быть пустым.")

        return name
