from .models import Counter, Convertion
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Convertion)
def create_new_calculation(sender, instance, created, **kwargs):
    
    if created:
        # get the object for the required count_paisa or create it if it doesn't exist
        count_object, created = Counter.objects.get_or_create(paisa=instance, defaults={"count": 0})
        count_object.count = count_object.count + 1
        count_object.save()
 
 


    
 
 

