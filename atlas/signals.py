import uuid
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, send_mass_mail
from .models import Counter, Convertion, ServiceA 
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
            unique_order_id = uuid.uuid4().hex
            message2 = (f'Your Order no : {unique_order_id}', 'Kuddos. You have purchased the perfect option for you.', 'sohamjani007@example.com', ['soham.sanjay@otocapital.in'])
            print(message2, len(message2))
            send_mass_mail([message2], fail_silently=False)
            service_object.cart = (f'CartID: {unique_order_id}')
            instance.save()
            service_object.save()
            print("!!!.Amount Verified")
        else:
            print(f"Newly created is :: {created}")







                


    
 
 

