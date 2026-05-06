from django import forms
from .models import Booking, Rating


class BookingForm(forms.Form):
    
    agreed_to_terms = forms.BooleanField(
        error_messages={'required': 'You must agree to the terms and conditions before paying.'}
    )
    subscription_months = forms.TypedChoiceField(
        coerce=int,
        choices=[],   
        widget=forms.RadioSelect()
    )

    def __init__(self, *args, max_months=1, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['subscription_months'].choices = [
            (m, f'{m} Month{"s" if m > 1 else ""}') for m in range(1, max_months + 1)
        ]


class RatingForm(forms.ModelForm):
    
    stars = forms.TypedChoiceField(
        coerce=int,
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)],
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Rating
        fields = ['stars', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here... (optional)'
            }),
        }
