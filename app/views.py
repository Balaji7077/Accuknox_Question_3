from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from .models import MyModel
# Create your views here.

def my_view(request):
    try:
        with transaction.atomic():
            # Create an object, this will trigger the post_save signal
            obj = MyModel.objects.create(name="Test Object")

            # Force a rollback by raising an exception
            raise Exception("Forcing a rollback")
    except Exception as e:
        print(f"Exception: {e}")

    return HttpResponse("Transaction attempted")
