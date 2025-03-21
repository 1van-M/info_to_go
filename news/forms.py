from django import forms

from news.models import Category


class ArticleForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255)
    content = forms.CharField(label='Содержание',
                              widget=forms.Textarea,
                              max_length=5000)
    category = forms.ModelChoiceField(label="Категория", queryset=Category.objects.all(), empty_label='Выберите категорию', widget=forms.Select(attrs={'class': 'form-control'}))
