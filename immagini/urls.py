from django.urls import path
from .views import SubidaImmagine

urlpatterns = [
    path('subida/', SubidaImmagine.as_view(), name='subida_img')
]