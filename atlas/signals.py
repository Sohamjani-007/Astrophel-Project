from .models import Counter, Convertion, ServiceA 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from atlas.choices import PaymentCurrencyStatusChoices, PaymentStatusChoices
 

@receiver(post_save, sender=Convertion)
def create_new_calculation(sender, instance, created, **kwargs):
    
    if created:
        # get the object for the required count_paisa or create it if it doesn't exist
        count_object, created = Counter.objects.get_or_create(paisa=instance, defaults={"count": 0})
        count_object.count = count_object.count + 1
        count_object.save()
 

@receiver(post_save, sender=Counter)
def order_item_paid(sender, instance, **kwargs):
    if instance.payment_status == "PENDING":
        print('Payment was Pending!!!!, pending other verifications')
        service_object, created = ServiceA.objects.get_or_create(payment_gross=instance, defaults={"match_currency": "RUPEE"})
        print('!!!! ServiceA Order object exists. Which is pending by customer.')
        if instance.paisa ==  service_object.payment_gross.paisa:
            instance.payment_status_to_payment_completed()
            instance.save()

            print("!!!.Amount Verified")
        else:
            print(f"Newly created is :: {created}")


                


    
 
 

