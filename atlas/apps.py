from django.apps import AppConfig
from django.db.models.signals import post_save


class AtlasConfig(AppConfig):
    name = 'atlas'
    def ready(self):
        from . import signals
        