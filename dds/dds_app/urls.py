from django.urls import path
from .views import (index,
                    financial_record,
                    status_list,
                    status_edit,
                    transaction_type,
                    category,
                    subcategory,
                    subcategory_edit,
                    subcategory_delete)

urlpatterns = [
    path('/', index, name='index'),
    path('financial_record/', financial_record, name='financial_record'),

    path('status_list/<int:pk>/edit', status_edit, name='form'),

    # path('index/references/', references, name='references'),

    path('status_list/', status_list, name='status_list'),
    # path('transaction_type/', transaction_type, name='transaction_type'),
    path('category_list/', category, name='category_list'),
    # path('subcategory/', subcategory, name='subcategory'),
    # path('subcategory/<int:pk>/edit/', subcategory_edit, name='subcategory_edit'),
    # path('subcategory/<int:pk>/delete/', subcategory_delete, name='subcategory_delete'),

]
