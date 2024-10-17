from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price',)

    def clean_name(self):
        clean_data = self.cleaned_data['name']

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in clean_data:
                raise forms.ValidationError(
                    'Вы не можете использовать запрещенные слова в названии продукта или описании продукта')
            return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data['description']

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in clean_data:
                raise forms.ValidationError(
                    'Вы не можете использовать запрещенные слова в названии продукта или описании продукта')
            return clean_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category',)


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version

        fields = ('product', 'version_name',)
