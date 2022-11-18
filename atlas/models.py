from django.db import models
import uuid as uuid
from model_utils.models import TimeStampedModel
from datetime import datetime
# Create your models here.

class Convertion(TimeStampedModel):
   class Meta:
        db_table = "paisa"

   paisa = models.IntegerField(blank=False, null=False)
   rupee = models.FloatField(blank=False, null=False)
   datetime = models.DateTimeField(default=datetime.now)

