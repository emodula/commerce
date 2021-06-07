from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, required=True)
    category = forms.CharField(label="Category" , max_length=50, required=False)
    description = forms.CharField(label="Description", widget=forms.Textarea, required=True)
    image = forms.FileField(required=False)
    bid_initial = forms.DecimalField(max_digits=7, decimal_places=2, required=True)
    
