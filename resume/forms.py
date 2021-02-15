from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Your Name*"})
    )
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': "Your Email*"})
    )
    subject = forms.CharField(required=False, max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Your Subject.."})
    )
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': "Your Message..."})
    )
