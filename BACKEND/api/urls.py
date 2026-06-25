
from django.urls import path
from . import views

urlpatterns = [
    path('transaction/',views.TransactionListCreateView.as_view(),name='transaction-list-create'),
    path('transaction/<uuid:id>/',views.TransationRetrieveUpdateDestroyView.as_view(),name='transaction-update-delete')
    
]