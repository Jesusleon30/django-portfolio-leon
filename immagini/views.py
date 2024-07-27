# aca en vista siempre la logica 

from rest_framework.views import APIView
from .serializers import ImmagineSerializers
from rest_framework.response import Response
from rest_framework import status


# class SubidaImmagine(APIView):
    # aca ira las get, post, patch, put, delete
    # def post(): #crear
    #     pass
    # def get(): # traer
    #     pass
    # def put(): # editar
    #     pass
    # def patch():  #editar
    #     pass
    # def delete():  # eliminar
    #     pass

class SubidaImmagine(APIView):
    
    def post(self, request):
        serializer = ImmagineSerializers(data=request.data)
        if serializer.is_valid():
            img_url = serializer.validated_data['img_url']  # cars.png
            img_url.name = 'images/' + img_url.name  #immagine/cars.png
            immagine = serializer.save()


            # ahora debemos obtener la URL de cloudinary
            img_url_full = immagine.img_url.url # .url es proprio de cloudinary/minube/carpeta/car.png
            immagine.img_url_full = img_url_full 
            immagine.save()

            # Actualizar nuestra respuesta de la URL
            respuesta = ImmagineSerializers(immagine)
            return Response(respuesta.data, status=status.HTTP_201_CREATED)








