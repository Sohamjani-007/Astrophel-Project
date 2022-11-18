from rest_framework import serializers
from atlas.models import Convertion

   
class AtlasSpaceshipSerializer(serializers.Serializer):
   """serializer, defined fields here."""
   central_system = serializers.CharField()
   tripod_measurement = serializers.IntegerField()

class RupeeToPaisaSerializer(serializers.ModelSerializer):
   """person related defined fields here."""
   class Meta:
      model = Convertion
      fields = ('paisa', 'datetime')
