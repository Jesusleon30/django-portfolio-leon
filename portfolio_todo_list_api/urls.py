from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tasks.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('storeapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('immagini.urls')),


        # esto nos permite authenticarnos:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # username y password
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'), # es para refrescar el token
    path('api/v1/', include('authentication.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

