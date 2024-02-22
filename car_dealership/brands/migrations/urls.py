from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrandListCreate.as_view(), name='brand-list-create'),
    path('<int:pk>/', views.BrandRetrieveUpdateDestroy.as_view(), name='brand-detail'),
]
