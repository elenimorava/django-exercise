from django.urls import path
from . import views

urlpatterns = [
    path('', views.DealerListCreate.as_view(), name='dealer-list-create'),
    path('<int:pk>/', views.DealerRetrieveUpdateDestroy.as_view(), name='dealer-detail'),
]
