from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["topic", "text"]
        labels = {"topic": "Temat", "text": "Treść"}
        widgets = {"text": forms.Textarea(attrs={"rows": 3, "cols": 40})}
