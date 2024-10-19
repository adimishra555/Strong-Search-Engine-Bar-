from django import forms
from .models import Product

class ProductSearchForm(forms.Form):
    name = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
    image = forms.ImageField(required=False)
    created_at = forms.DateTimeField(required=False)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']



