from django.urls import path
from .views import (index,
                    financial_record,
                    status_list,
                    status_edit,
                    transaction_type,
                    category_list,
                    category_edit,
                    subcategory,
                    subcategory_edit,
                    subcategory_delete)

urlpatterns = [
    path('', index, name='index'),
    path('financial_record/', financial_record, name='financial_record'),
    path('status_list/', status_list, name='status_list'),
    path('status_list/<int:pk>/edit/', status_edit, name='form'),
    path('category_list/', category_list, name='category_list'),
    path('category_list/<int:pk>/edit/', category_edit, name='form'),

    # path('index/references/', references, name='references'),
    # path('transaction_type/', transaction_type, name='transaction_type'),
    # path('subcategory/', subcategory, name='subcategory'),
    # path('subcategory/<int:pk>/edit/', subcategory_edit, name='subcategory_edit'),
    # path('subcategory/<int:pk>/delete/', subcategory_delete, name='subcategory_delete'),

]
