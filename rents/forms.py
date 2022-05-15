from django import forms
from .models import Rent


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('content', 'tag', 'rent_type', 'location', 'price')
    widgets= {
        'content': forms.Textarea(attrs={
            'class': "form-control",
                'style': 'max-width: 700px; height:500px; overflow: auto; resize:none;',
                'placeholder': '상세 내용을 작성해주세요',
                'overflow-wrap': 'break-word' ,
        })
    }
    