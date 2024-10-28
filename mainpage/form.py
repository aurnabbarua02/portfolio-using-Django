from django import forms

class sendmessageform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%; margin-top: 5px;'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'width: 100%; margin-top: 5px;'}), required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:100%; margin-top: 5px;'}), required=False)