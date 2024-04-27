from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, AvailabilityViewSet, AppointmentViewSet, BulkDeleteDoctors
from . import views

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'availability', AvailabilityViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/doctors/bulk-delete/', BulkDeleteDoctors.as_view(), name='bulk_delete_doctors'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
]
