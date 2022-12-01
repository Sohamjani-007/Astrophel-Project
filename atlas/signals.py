import uuid
from django.conf import settings
from django.db.models.signals import post_save
from twilio.rest import Client
from django.dispatch import receiver
from django.core.mail import send_mass_mail
from .models import Counter, Convertion, ServiceA, User




@receiver(post_save, sender=Convertion)
def create_new_calculation(sender, instance, created, **kwargs):
    
    if created:
        # get the object for the required count_paisa or create it if it doesn't exist
        count_object, created = Counter.objects.get_or_create(paisa=instance, defaults={"count": 0})
        count_object.count = count_object.count + 1
        count_object.save()
 

@receiver(post_save, sender=Counter)
def order_item_paid(sender, instance, **kwargs): 
    user_obj = User.objects.last()
    if instance.payment_status == "PENDING":
        print('Payment was Pending!!!!, pending other verifications')
        service_object, created = ServiceA.objects.get_or_create(payment_gross=instance, reported_by=user_obj.username, defaults={"match_currency": "RUPEE"})
        print('!!!! ServiceA Order object exists. Which is pending by customer.')
        if instance.paisa ==  service_object.payment_gross.paisa:
            instance.payment_status_to_payment_completed()
            unique_order_id = uuid.uuid4().hex
           
            # The below code is Email Impletation, of the Service Cart Created
            message2 = (f'Your Order no : {unique_order_id}', 'Kuddos. You have purchased the perfect option for you.', 'sohamjani007@example.com', ['soham.sanjay@otocapital.in'])
            print(message2, len(message2))
            send_mass_mail([message2], fail_silently=False)
            service_object.cart = (f'CartID: {unique_order_id}')
            instance.save()
            service_object.save()
            print("!!!.Amount Verified")

            # The below code is Twilio SMS Impletation, of the Service Cart Created
            # message_to_broadcast = (f"Your Order no : {unique_order_id}, Have you checked out this awesome website."
            #                                     "yet? Click to enter wonderland: https://www.internetlivestats.com/")
            # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            # for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
            #     if recipient:
            #         client.messages.create(to=recipient,
            #                             from_=settings.TWILIO_NUMBER,
            #                             body=message_to_broadcast)
        else:
            print(f"Newly created is :: {created}")







                


    
 
 

