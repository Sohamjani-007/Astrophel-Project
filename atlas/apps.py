from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class AtlasConfig(AppConfig):
    name = 'atlas'
    def ready(self):
        from . import signals
        