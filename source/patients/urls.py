from django.urls import path
from .views import PatientListView


urlpatterns = [
    path('patients/', PatientListView.as_view(), name='token_obtain_pair'),# Эндпоинт для получения списка пациентов
]
