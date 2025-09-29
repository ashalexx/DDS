from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import (FinancialRecord,
                     TransactionType,
                     Status,
                     Category,
                     Subcategory)
from .forms import (FinancialRecordForm,
                    StatusForm,
                    TransactionTypeForm,
                    CategoryForm,
                    SubcategoryForm)


def index(request):
    financial_record = FinancialRecord.objects.all()
    return render(request,
                  'dds_app/index.html',
                  {'financial_record': financial_record})


def financial_record(request):
    financial_record = FinancialRecord.objects.all()
    if request.method == 'POST':
        form = FinancialRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FinancialRecordForm()
    return render(request,
                  'dds_app/financial_record.html',
                  {'form': form, 'financial_record': financial_record})


def status_list(request):
    status = Status.objects.all()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm()
    return render(request,
                  'dds_app/status_list.html',
                  {'form': form, 'status': status})


def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обновлена!')
            return redirect('status_list')
    else:
        form = StatusForm(instance=status)
    return render(request,
                  'dds_app/form.html',
                  {
                      'form': form,
                  })


def transaction_type(request):
    transaction_type = TransactionType.objects.all()
    if request.method == 'POST':
        form = TransactionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_type')
    else:
        form = TransactionTypeForm()
    return render(request,
                  'dds_app/transaction_type.html',
                  {'form': form, 'transaction_type': transaction_type})


def category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    return render(request,
                  'dds_app/category.html',
                  {'form': form, 'category': category})


def subcategory(request):
    subcategory = Subcategory.objects.all()
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory')
    else:
        form = SubcategoryForm()
    return render(request,
                  'dds_app/subcategory.html',
                  {'form': form, 'record': subcategory})


def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обновлена!')
            return redirect('subcategory')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request,
                  'dds_app/form.html',
                  {
                      'h1': 'Изменить подкатегорию',
                      'button': 'Изменить',
                      'form': form,
                      'record': [subcategory],
                  })


def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    # form = SubcategoryForm()
    if request.method == 'POST':
        subcategory.delete()
        messages.success(request, 'Запись успешно удалена!')
        return redirect('subcategory')
    return render(request,
                  'dds_app/record_confirm_delete.html',
                  {'record': subcategory})
