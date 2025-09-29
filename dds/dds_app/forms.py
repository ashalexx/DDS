from django import forms
from .models import FinancialRecord, Status, TransactionType, Category, Subcategory


class FinancialRecordForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = [
            'created_date',
            'status',
            'transaction_type',
            'category',
            'subcategory',
            'amount',
            'comment'
        ]
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите статус записи',
                'required': True
             }
             ),
            'created_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'дд.мм.гггг'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'form-control',
                    'placeholder': 'Введите комментарий (необязательно)'
                }
            ),
            # 'status': forms.Select(attrs={'class': 'form-control'}),
            # 'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            # 'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
            # 'subcategory': forms.Select(attrs={'class': 'form-control', 'id': 'id_subcategory'}),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'min': '0.01',
                    'placeholder': '0.00'
                }
            ),
        }
        labels = {
            'created_date': 'Дата операции',
            'transaction_type': 'Тип операции',
            'amount': 'Сумма (рубли)',
        }
        help_texts = {
            'comment': 'Необязательное поле',
            'amount': 'Введите сумму в рублях, например: 1000.50',
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'name'
        ]
        widgets = {
            'created_at': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'дд.мм.гггг'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    # 'rows': 1,
                    # 'class': 'form-control',
                    'placeholder': 'Введите название статуса'
                }
            ),
        }
        labels = {
            'name': 'Статус',
        }


class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = [
            'name'
        ]
        widgets = {
            'created_at': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'дд.мм.гггг'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название транзакции'
                }
            ),
        }
        labels = {
            'name': 'Тип транзакции',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
        widgets = {
            'created_at': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'дд.мм.гггг'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название категории'
                }
            ),
        }
        labels = {
            'name': 'Категория',
        }


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        labels = {
            'name': 'Название подкатегории',
            'category': 'Категория'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название подкатегории'
            }),
            'category': forms.Select()
        }
