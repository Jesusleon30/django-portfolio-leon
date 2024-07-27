from rest_framework import serializers
from .models import Immagine # importamos el modelo immagine

class ImmagineSerializers(serializers.ModelSerializer):

    # desealizar
    # convertir a json
    # validaciones

    img_url_full = serializers.CharField(source = 'img_url', read_only =True)

    class Meta:
        model = Immagine
        fields = ['id', 'name', 'img_url', 'img_url_full']
        # o sino se puede poner  __all__

