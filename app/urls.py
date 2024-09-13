from django.urls import path
from . import views

urlpatterns = [
    path('test-transaction/', views.my_view, name='test_transaction'),
]
