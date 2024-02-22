from django.urls import path
from . import views

urlpatterns = [
    path('', views.PurchaseListCreate.as_view(), name='purchase-list-create'),
    path('<int:pk>/', views.PurchaseRetrieveUpdateDestroy.as_view(), name='purchase-detail'),
]
