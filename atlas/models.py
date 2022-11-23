
import uuid as uuid
from datetime import datetime
from django.db import models
from django_fsm import FSMField, transition
from django_fsm_log.decorators import fsm_log_by
from model_utils.models import TimeStampedModel
from atlas.choices import PaymentStatusChoices,PaymentCurrencyStatusChoices


# Create your models here.
class Convertion(TimeStampedModel):
   class Meta:
        db_table = "paisa"

   paisa = models.IntegerField(blank=False, null=False)
   rupee = models.FloatField(blank=False, null=False)
   datetime = models.DateTimeField(default=datetime.now)


class Counter(TimeStampedModel):
     paisa = models.ForeignKey(Convertion, on_delete=models.CASCADE ,related_name='counter_paisa')
     count = models.IntegerField(blank=False, null=False)
     payment_status = FSMField(choices=PaymentStatusChoices.choices, null=True, blank=True, default="PENDING", protected=True)
     @transition(
        field=payment_status,
        source=[PaymentStatusChoices.PAYENT_PENDING],
        target=PaymentStatusChoices.PAYMENT_COMPLETED)
     def payment_status_to_payment_completed(self):
        """Requested amount matched and pending amount got completed."""
        ...

class ServiceA(TimeStampedModel):
     cart = models.CharField(max_length=500, blank=False, null=False, help_text="add_items_to_cart")
     payment_gross = models.ForeignKey(Counter, on_delete=models.CASCADE, related_name='service_payment_gross')
     match_currency = FSMField(choices=PaymentCurrencyStatusChoices.choices, null=True, blank=True, default=None, protected=True)
     # paisa_paid = models.ForeignKey(Convertion, on_delete=models.CASCADE ,related_name='service_paisa_paid')
