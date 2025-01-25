from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),# Эндпоинт для получения токена
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# Эндпоинт для обновления токена
]
