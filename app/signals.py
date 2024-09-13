from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import threading

@receiver(post_save, sender=MyModel)
def my_model_saved(sender, instance, **kwargs):
    print(f"Signal handler: Object saved in thread {threading.current_thread().name}")
